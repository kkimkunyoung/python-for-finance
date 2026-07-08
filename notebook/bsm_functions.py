#
# 블랙-숄즈-머튼 모형에 의한
# 유러피안 콜 옵션의 가치 평가
# (베가함수와 내재 변동성 추정 포함)
# bsm_functions.py
#
# (c) Dr. Yves J. Hilpisch
# Python for Finance, 2nd edition
#

def bsm_call_value(S0, K, T, r, sigma):
    ''' BSM 모형에 의한 유러피안 콜 옵션의 가치 평가 해석적 공식

    인수
    ==========
    S0: float
        초기 주가/지수 수준
    K: float
        행사가
    T: float
        만기 (연수로 계산)
    r: float
        고정 단기 무위험 이자율
    sigma: float
        변동성
    
    반환값
    ==========
    value: float
        유러피안 콜 옵션의 현재 가치
    '''
    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma * sigma) * T) / (sigma * sqrt(T))

    # stats.norm.cdf --> 정규분포의 누적분포함수
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))

    return value

def bsm_vega(S0, K, T, r, sigma):
    ''' BSM 모형에 따른 유러피안 옵션의 베가

    인수
    ==========
    S0: float
        초기 주가/지수 수준
    K: float
        행사가
    T: float
        만기 (연수로 계산)
    r: float
        고정 단기 무위험 이자율
    sigma: float
        변동성
    
    반환값
    ==========
    value: float
        BSM 공식의 변동성에 대한 편미분, 즉 베가
    '''
    from math import log, sqrt
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrt(T))
    vega = S0 * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(T)

    return vega

# 내제 변동성 함수
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_ext, it=100):
    ''' BSM 모현에 따른 유러피안 콜 옵션의 내재 변동성

    인수
    ==========
    S0: float
        초기 주가/지수 수준
    K: float
        행사가
    T: float
        만기 (연수로 계산)
    r: float
        고정 단기 무위험 이자율
    sigma_ext: float
        내재 변동성의 추정치
    it: integer
        반복 횟수
    
    반환값
    ==========
    sigma_est: float
        수치적으로 추정한 내재 변동성
    '''
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0) / bsm_vega(S0, K, T, r, sigma_est))
    return sigma_est
#import module
#module.price(3)
#module.price_moring(5)
#module.price_soldier(13)

#import module as mv #별명설정
#mv.price_soldier(2)

#from module import * # * = module을 모두 사용
#price_soldier(2)

from module import price as p #필요한 정보만 improt 가능 as 로 별명설정가능
p(2)

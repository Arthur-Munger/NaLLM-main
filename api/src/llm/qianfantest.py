from llm.qianfanai import QianFanChat
x = QianFanChat( "ALTAKib1IkhOp3M7z2dvWtZlf1", "28c21eba119d4fe18015d2d179017523")
re = x.generate([{"role": "user", "content": "3+4 = ？"}])
print(re)
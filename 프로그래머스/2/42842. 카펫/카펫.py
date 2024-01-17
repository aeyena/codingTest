def solution(brown, yellow):
    total = brown + yellow #총 카펫 수 
    for i in range(1, int((total+1)/2)): #효율을 위해 절반만 
        if(total%i==0): 
            pairOne = int(total/i) #i의 짝꿍 구하기(약수)
            if((i+pairOne)*2 - 4 == brown): #테두리 카펫수로 답 구하기
                return [pairOne,i]
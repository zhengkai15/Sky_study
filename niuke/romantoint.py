# class Solution:
#     def romanToInt(self , s ):
#         # write code here
#         dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         Sum=0
#         # print(dic.values())
#         # print(dic.get('I'))
#         for item in dic.keys():
#             Sum+=s.count(item)*dic[item]
#         return Sum
class Solution:
    def intToRoman(self, num: int) -> str:
        #建立特殊情况下字符和对应数字的字典--special_dict
        special_dict={4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        sub_str1=sub_str2=sub_str3=sub_str4=sub_str5=sub_str6=sub_str7=''
        #建立字符和对应数字的字典--luoma_dict
        luoma_dict={}
        character_list=['I','V','X','L','C','D','M']
        value_list=[1,5,10,50,100,500,1000]
        for i in range(7):
            luoma_dict[value_list[i]]=character_list[i]
        #对给定的输入整数进行取整运算，并判断是否存在特殊情况下的数字
        while num:
            sub_str1=(num//1000)*luoma_dict[1000]
            sub_value1=(num//1000)*1000
            num=num-sub_value1
            if num-900>=0:
                sub_str2=special_dict[900]
                num=num-900
            else:
                sub_str2=(num//500)*luoma_dict[500]
                sub_value1=(num//500)*500
                num=num-sub_value1
                
            if (num//100)==4:
                sub_str3=special_dict[400]
                num=num-400
            else:
                sub_str3=(num//100)*luoma_dict[100]
                sub_value1=(num//100)*100
                num=num-sub_value1
            if num-90>=0:
                sub_str4=special_dict[90]
                num=num-90
            else:
                sub_str4=(num//50)*luoma_dict[50]
                sub_value1=(num//50)*50
                num=num-sub_value1

            if (num//10)==4:
                sub_str5=special_dict[40]
                num=num-40
            else:
                sub_str5=(num//10)*luoma_dict[10]
                sub_value1=(num//10)*10
                num=num-sub_value1

            if num-9>=0:
                sub_str6=special_dict[9]
                num=num-9
            else:
                sub_str6=(num//5)*luoma_dict[5]
                sub_value1=(num//5)*5
                num=num-sub_value1
                                
            if num==4:
                sub_str7=special_dict[4]
                num=num-4
            else:
                sub_str7=num*luoma_dict[1]
                sub_value1=num
                num=num-sub_value1
        return (sub_str1+sub_str2+sub_str3+sub_str4+sub_str5+sub_str6+sub_str7)    




if __name__ == '__main__':
	s=Solution()
	# print(s.romanToInt('DVIII'))
	print(s.intToRoman(9))
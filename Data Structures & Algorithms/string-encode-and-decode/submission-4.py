class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""

        for s in strs:
            leng = 0
            single_str = ""
            for c in s:
                single_str = single_str + c
                leng += 1
            output_str = output_str + str(leng) + " " + single_str
        return output_str

    def decode(self, s: str) -> List[str]:
        output_strs = []
        single_str = ""

        leng = ""
        leng_int = 0
        started = False

        for c in s:
            if started:
                if leng_int < 1:
                    started = False
                    output_strs.append(single_str)
                    single_str = ""
                    leng = c
                else:
                    print(c, leng_int)
                    single_str = single_str + c
                    leng_int = leng_int - 1

            else:
                if c == " ":
                    started = True
                    leng_int = int(leng)
                    print (leng_int)
                else:
                    leng = leng + c

        if len(s) > 0:
            output_strs.append(single_str)

        return output_strs

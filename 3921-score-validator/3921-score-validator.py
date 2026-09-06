class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ts=0
        c=0
        i=0
        while i<len(events) and c<10:
            if events[i].isdigit():
                ts+=int(events[i])
            elif events[i]=="W":
                c+=1
            elif events[i]=="WD" or events[i]=="NB":
                ts+=1
            i+=1
        return [ts,c] 
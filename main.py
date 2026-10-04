import re,sys,json
LABELS={'billing':['price','bill','refund','payment','invoice'],'technical':['error','bug','crash','login','slow'],'shipping':['delivery','ship','tracking','order'],'account':['password','profile','account','delete']}
def classify(t):
 w=set(re.findall(r'[a-z]+',t.lower())); scores={k:len(w&set(v)) for k,v in LABELS.items()}; label=max(scores,key=scores.get); return {'intent':label if scores[label] else 'other','scores':scores}
if __name__=='__main__': print(json.dumps(classify(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Text: ')),indent=2))
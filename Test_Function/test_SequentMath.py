import difflib

a = 'นครxxx'
b = 'นครปฐม'
#b = 'นครพนม'

seq = difflib.SequenceMatcher(None,a,b)
d = seq.ratio()*100
print(d) 

# หลักการ ของ SequenceMatcher คือการเปรียบเทียบตำแหน่งของคำทีละตัวมาใช้ในการคำนวณ
# และหารจากจำนวนอักษรทั้งหมดเพื่อมาทำเป็นคะแนนอ้างอิงความถูกต้อง

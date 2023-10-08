import requests 
from bs4 import BeautifulSoup
import csv


res = requests.get("https://www.91mobiles.com/top-10-mobiles-in-india")

soup = BeautifulSoup(res.text,'html.parser')


title = soup.title.string

#-----------------Phone-Image--------------------------#
ImageLink1=[]
ImageLink2=[]

box_img = soup.find_all(class_="finder_pro_image fimage gaclick")

for desc in box_img:
	img=[]
	if desc.get('src')!= None:
		src_value = desc.get('src')
	else :
		src_value = desc.get('data-src')
	ImageLink1.append(src_value.replace('//',''))	
	ImageLink2.append(src_value.replace('//','').replace('medium-1.jpg?tr=q-80','hres-2.jpg'))
	
#-----------------Phone-Name--------------------------#

box_pn = soup.find_all(class_="filter-grey-bar")

#List To Store All The Names of Phone on this Page
phoneName=[]
for x in box_pn :
	if x.a == None :
		continue
	temp=x.a.getText().replace('\n','').lstrip().rstrip()
	phoneName.append(temp)

#-----------------Price-----------------------------#

box_pr = soup.find_all(class_="price price_padding")
price = [ x.getText().replace('Rs','').replace(',','').replace('.','') for x in box_pr ]


#-----------------Expert Comment---------------------#
ExpertComment=[]

box_ec = soup.find_all(class_="exp_comnt_pnl")
for desc in box_ec:
	temp = desc.getText().splitlines()
	ExpertComment.append(temp[2].lstrip().rstrip())


#-----------------Specification---------------------#
Performance =[]
Display =[]
Camera =[]
Battery =[]
	
box_sc = soup.find_all(class_="filter-grey-bar filter_gray_bar_margin grey_bar_custpage")

for boxe in box_sc:
	sub_box = boxe.find_all(class_="left specs_li")
	for x in sub_box:
		ans=x.getText()
		if 'Performance' in ans:
			LI=[]
			for a in x.find_all("label"):
				LI.append(a.getText())		
			ans=""
			for i in LI:
		        	ans= ans + i +'\n'
			Performance.append(ans)
		if 'Display' in ans:
			LI=[]
			for a in x.find_all("label"):
				LI.append(a.getText())
			ans=""
			for i in LI:
				ans= ans + i +'\n'				
			Display.append(ans)	
		if 'Camera' in ans:
			LI=[]
			for a in x.find_all("label"):
				LI.append(a.getText())
			ans=""
			for i in LI :
		        	ans= ans + i +'\n'				
			Camera.append(ans)	
		if 'Battery' in ans:
			LI=[]
			for a in x.find_all("label"):
				LI.append(a.getText())
			ans=""
			for i in LI :
		        	ans= ans + i +'\n'									
			Battery.append(ans)


merged_data = list(zip(phoneName, ImageLink1, ImageLink2, price, ExpertComment,Performance, Display, Camera, Battery))

csv_file_name = f"{title}.csv"

with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header row
    csv_writer.writerow(['Phone Name', 'Image Link 1', 'Image Link 2', 'Price', 'Expert Comment', 'Performance', 'Display', 'Camera', 'Battery'])
    
    # Write data rows
    csv_writer.writerows(merged_data)





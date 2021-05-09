from docxtpl import DocxTemplate
from randomuser import RandomUser

def genDocument(title, user, company):
    tpl = DocxTemplate("tpl.docx")
    context = {
        "title": title,
        "user": user, 
        "company_name": company
    }
    tpl.render(context)
    file_path = './document/'
    try:
        tpl.save(f'{file_path}generate_{user}_document.docx')
        return 'success'
    except Exception as e:
        return str(e)



# for i in range(2):
#     user = RandomUser().get_first_name()
#     genDocument('mytitle', user , f'MY {user} Company')

# ret = genDocument('xxx', 'myusername', 'myCOMPANY')
# print(ret)
    
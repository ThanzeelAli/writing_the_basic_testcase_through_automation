import openpyxl
from openpyxl import Workbook

wb=Workbook()
wb['Sheet'].title="flipKart"
sh=wb.active
sh["A1"].value="Epic"
sh["A2"].value="In this epic is check the login page are work when the user can enter the website home page"
sh["B1"].value="User story ID"
sh["B2"].value="US001"
sh["B3"].value="US005"
sh["B4"].value="US007"
sh["C1"].value="Title"
sh["C2"].value="Register"
sh["C3"].value="login"
sh["C4"].value="logout"
sh["D1"].value="User story"
sh["D2"].value='''As the first time user visit the website
                     I want to register my account
                     So thet i can login the application'''
sh["D3"].value="As the register" \
               "  I want to login the website" \
               "  so that i can see the purchase site"
sh["D4"].value="As the register " \
               "  I want to logout the website" \
               "  So that user can see the log in page"
sh["E1"].value="Status"
sh["E2"].value="new"
sh["E3"].value="new"
sh["E4"].value="new"
sh["F1"].value="Update states"
sh["F2"].value="A new user should able to rfegister the website"
sh["F3"].value="A system can allow only valid information "
sh["F4"].value="The web can lagout"
wb.save("Test Senarious.xlsx")


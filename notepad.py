from pywinauto.application import Application

def testNotepad1 ():
    app = Application(backend="uia").start("notepad.exe")
    app.UntitledNotepad.menu_select("File->PageSetup")
    ##app.UntitledNotepad.Page.Cancel.click
    ##app['UntitledNotepad']['Page Setup'].print_control_identifiers()
    x=app['UntitledNotepad']['Page Setup']
    x.Button3.click()
    app.UntitledNotepad.menu_select("Edit->Paste")
    app.UntitledNotepad.menu_select("File->SaveAs")
    y=app['UntitledNotepad']['Save As']
    ##y.print_control_identifiers()
    ##y.ComboBox3.select("UTF-8")
    ##y.print_control_identifiers()
    y.edit41.set_text("test1.txt")
    y.Save.click()
    app.NotepadDialog.menu_select("File->Exit")
    ##app.UntitledNotepad.print_control_identifiers()
    ##app.Dialog.Button2.click()  
    print(" Uscito")
    return;

testNotepad1()
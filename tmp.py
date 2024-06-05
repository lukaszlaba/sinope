def get_staad_psas_points_from_dxf():
    global dxfopendir
    #---
    #dxffilepath = QtWidgets.QFileDialog.getOpenFileName(caption = 'Open excel file', directory = dxfopendir, filter = ".dxf' (*.dxf)")[0]
    dxffilepath = 'C:/Users/Lenovo/Dropbox/PYAPPS_STRUCT/SOURCE_SINOPE/psas_staad.dxf'
    dxffilepath = str(dxffilepath)
    if not dxffilepath == '':
        dxfopendir = os.path.dirname(dxffilepath)
    #---
    print(dxffilepath)
    dwg = ezdxf.readfile(dxffilepath)
    #--deleting circles
    to_delete = []
    for e in dwg.modelspace():
            if e.dxftype() == 'CIRCLE':
                print(e)
                to_delete.append(e)
    for e in to_delete:
        dwg.modelspace().delete_entity(e)

    # for e in dwg.modelspace():
    #     if e.dxftype() == 'TEXT':
    #         print(e.dxf.text, e.dxf.insert)


    for e in dwg.modelspace():
        for j in dwg.modelspace():
            if e.dxftype() == 'TEXT' and j.dxftype() == 'TEXT':
                if abs(abs(e.dxf.insert[0])+abs(e.dxf.insert[1])+abs(e.dxf.insert[2]) - (abs(j.dxf.insert[0])+abs(j.dxf.insert[1])+abs(j.dxf.insert[2]))) < 0.001:
                    if str(e.dxf.text) != str(j.dxf.text):
                        if not e.dxf.text.isnumeric():
                        #print(e.dxf.text, e.dxf.insert, j.dxf.text, j.dxf.insert)
                            print(e.dxf.text,'@',j.dxf.text)
                            dwg.modelspace().add_circle(e.dxf.insert, radius=0.5)
    dwg.save()




#print(e.dxf.text, e.dxf.insert[0])
#(-1074.456287169948, -3775.77613600026, 1190.092955003295)
#(-1074.456287169948, 1190.092955003295, 3775.77613600026)
#FAB2-AW-31_C111 (-1088.37, -3773.41, 1190.49)
#1313 (-1088.37, 1190.489999999999, 3773.41)







get_staad_psas_points_from_dxf()

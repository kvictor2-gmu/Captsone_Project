#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def embedded_image(path):
    import jpype
    import asposecells
    import os.path
    
    #check if JVM is started, start JVM if not
    if jpype.isJVMStarted() == 0:
        jpype.startJVM()
        
    from asposecells.api import Workbook
    
    output = 0
    #check if file is excel file
    root, extension = os.path.splitext(path)
    
    if extension not in ('.xlsx','.xlsm','.xls'):
        return(output)
     
    workbook = Workbook(path)
    sheet_count = workbook.getWorksheets().getCount()
    
    #check if worksheet exist
    if sheet_count == 0:
        return(output)
    
    #loop through worksheets
    for i in range(0,sheet_count):
        active_sheet = workbook.getWorksheets().get(i)
        
        # get picture attribute information
        pic_set_count = 0
        pic_set = active_sheet.getPictures()
        pic_set_count = pic_set.getCount()
        #print(pic_set_count)
        
        # go to next loop if there are no picture in sheet
        if pic_set_count == 0:
            next
        else:
            output = 1
            
            #loop through all pictures
            #for y in range(0,pic_set_count):
            
                #ref: https://reference.aspose.com/cells/python-java/asposecells.api/Picture
                #pic = active_sheet.getPictures().get(y)
                
                # dict[path,worksheet index, picture index, metadata]
                #info_dict[path,i,y,'width'] = pic.getOriginalWidth()
                #info_dict[path,i,y,'height'] = pic.getOriginalHeight()

    return(output)


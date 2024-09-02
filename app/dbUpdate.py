import argparse,settings
from main.models import Components,ComponentCategorys

def main(argv):

    #p=argparse.ArgumentParser(description="""
    #                          Обновлыет имена файлов отображений
    #                            в базе данных
    #                          """)
    #p.add_argument("indirectory")

    indir=settings.DEFAULTCHARTDIRECTORY
    if len(argv) == 1:
        indir=settings.DEFAULTCHARTDIRECTORY
    elif len(argv) == 2:
        indir = argv[1]
    else:
        raise SystemExit(f'Usage : python {argv[0]} inputfile outputfile\n')    
    #outputfile = argv[2]

    from pathlib import Path
    p = Path(indir)
    #projectnames=os.listdir(indir,)
    projectpathes = [projectpath for projectpath in p.iterdir() if projectpath.is_dir()]
    projectDBCategorys= ComponentCategorys.objects.all()
    projectCategorys = [projectDBCategory.name for projectDBCategory in projectDBCategorys]
    for projPath in projectpathes:
        projectCategoryPathes = [categoryPath for categoryPath in projPath.iterdir() if categoryPath.is_dir()]
        for projectCategoryPath in projectCategoryPathes:
            #filePathes=projectCategoryPath.glob('*.jpg')
            for projectCategory in projectCategorys:
                if projectCategory=="Компоновка" :
                    filePathes=projectCategoryPath.glob('*.jpg')
                    if filePathes != None :
                        for filePath in filePathes:
                            if filePath.name==projPath.name :
                                if Components.objects.filter(sketch=filePath) == None :
                                    Components.objects.create(sketch=filePath,componentCategory="Компоновка")                                                     

if __name__ == '__main__':
    import sys
    main(sys.argv)
import csv
import operator
import pdb
import os

def main(filename):

    with open(filename) as papers:
        music_tech_papers = csv.DictReader(papers, dialect='excel-tab')
        #get items in column
        f = music_tech_papers.fieldnames

        paths = []
        accumulated_table = []
        num_paper = 0
        for entry in music_tech_papers:
            # get attributes from table
            mother_group = entry[f[0]]
            child_group = entry[f[1]]
            publication_year = entry[f[2]]
            author = entry[f[3]]
            title = entry[f[4]]
            title_url	= entry[f[5]]
            abstract= entry[f[6]]
            source_code	= entry[f[7]]
            source_code_url= entry[f[8]]
            data_set1 = entry[f[9]]
            data_set_url1 = entry[f[10]]
            data_set2 = entry[f[11]]
            data_set_url2 = entry[f[12]]
            data_set3 = entry[f[13]]
            data_set_url3 = entry[f[14]]
            demo1 = entry[f[15]]
            demo_url1 = entry[f[16]]
            demo2 = entry[f[17]]
            demo_url2 = entry[f[18]]

            path = file_destination(mother_group, child_group)
            paths.append(path)

            create_md(path, publication_year, title, title_url, author,
                      abstract, data_set1, data_set_url1, data_set2, data_set_url2, data_set3, data_set_url3,
                      source_code, source_code_url, demo1, demo_url1, demo2, demo_url2)

            group_dataset_table(mother_group, child_group,
                     data_set1, data_set_url1,
                     data_set2, data_set_url2,
                     data_set3, data_set_url3,
                     accumulated_table)

            num_paper += 1

    print("num_paper", num_paper)

    paths = list(dict.fromkeys(paths))

    print("accumulated_table", accumulated_table)
    for path in paths:
        merge_mds(path)

# TODO dataset table can be added in next dev phase
# def dataset_table(accumulated_table):
#     first_column = "| Mother Group | Child Group | Data set |"



def group_dataset_table(mother, child,
                     data_set1, data_set_url1,
                     data_set2, data_set_url2,
                     data_set3, data_set_url3,
                     accumuated_list):

    temp = [data_set1, data_set2, data_set3]
    content = [i for i in temp if i != '']

    if len(content) == 0:
        return accumuated_list

    elif len(content) == 1:
        table_line = '|' + mother + '|' + child + '|[' + data_set1 + '](' + data_set_url1 + ')|' \
                    + '|' + '|' + '|' +'|' \
                    + '|' +  '|' + '|' + '|'
        accumuated_list.append(table_line)
    elif len(content) == 2:
        table_line = '|' + mother + '|' + child + '|[' + data_set1 + '](' + data_set_url1 + ')|' \
                     + '|[' + data_set2 + '](' + data_set_url2 + ')|' \
                     + '|' + '|' + '|' + '|'
        return accumuated_list.append(table_line)
    elif len(content) == 3:
        table_line = '|' + mother + '|' + child + '|' + data_set1 + '|' + data_set_url1 + '|' \
                     + '|[' + data_set2 + '](' + data_set_url2 + ')|' \
                     + '|[' + data_set3 + '](' + data_set_url3 + ')|'
        return  accumuated_list.append(table_line)


# '|' +  + '|' +  + '|' + + '|' + + '|'


    



def merge_mds(path_to_mds):
    md_list = os.listdir(path_to_mds)
    readme_name = "README.md"

    with open(path_to_mds+readme_name, "w+") as readme:
        for md in md_list:
            with open(path_to_mds+md) as temp:
                readme.write(temp.read())
            if md != "README.md":
                os.remove(path_to_mds+md)

def file_destination(mother_group, child_group,
                     root_path="/home/hk/Documents/Workspace/proj/paper_archive"):
    return root_path + '/' + mother_group + '/' + child_group + '/'

def create_md(path, publication_year, title, title_url, author,
                      abstract, data_set1, data_set_url1, data_set2, data_set_url2, data_set3, data_set_url3,
                      source_code, source_code_url, demo1, demo_url1, demo2, demo_url2):

    filename = title + ".md"

    data = [data_set1, data_set_url1, data_set2, data_set_url2, data_set3, data_set_url3]
    source = [source_code, source_code_url]
    demo = [demo1, demo_url1, demo2, demo_url2]

    with open(path+filename,"w+" ) as paper_md:

        line_title = "# " + ' ' + '['+ title +']' +'('+ title_url+')' + '\n'
        line_author = "Author: " + author + '\n' + '\n'
        line_year = "Year: " + publication_year + '\n'
        line_abstract = ">Abstract: " + abstract +'\n' + '\n'
        line_dataset = "Data Set: "
        line_sourcecode = "Source Code: "
        line_demo = "Demo: "

        for i in range(0,len(data)):
            if data[i] == '':
                if i == 0:
                    line_dataset += "Not availabe, "
                    break
                else:
                    break
            elif i % 2 == 0:
                line_dataset += '['+ data[i] +']' + '(' + data[i+1] +'), '
        line_dataset = line_dataset[:-2] + "\n\n"

        for i in range(0,len(source)):
            if source[i] == '':
                if i == 0:
                    line_sourcecode += "Not availabe, "
                    break
                else:
                    break
            elif i % 2 == 0:
                line_sourcecode += '['+ source[i] +']' + '(' + source[i+1] +'), '
        line_sourcecode = line_sourcecode[:-2]  + "\n\n"

        for i in range(0,len(demo)):
            if demo[i] == '':
                if i == 0:
                    line_demo += "Not availabe, "
                    break
                else:
                    break
            elif i % 2 == 0:
                line_demo += '['+ demo[i] +']' + '(' + demo[i+1] +'), '
        line_demo = line_demo[:-2]  + "\n\n"

        paper_md.write(line_title)
        paper_md.write(line_author)
        paper_md.write(line_year)
        paper_md.write(line_abstract)
        paper_md.write(line_dataset)
        paper_md.write(line_sourcecode)
        paper_md.write(line_demo)



def sort_papers_by_year(filename):
    with open(filename, "r+") as mixing:
        mixing_tsv = csv.DictReader(mixing, dialect='excel-tab')
        f = mixing_tsv.fieldnames

        sorted_mixing = sorted(mixing_tsv, key=operator.itemgetter('Publication Year'), reverse=True)

        mixing.seek(0)
        writer = csv.DictWriter(mixing, delimiter='\t', dialect='excel-tab', fieldnames=f)
        writer.writeheader()
        for row in sorted_mixing:
            writer.writerow(row)
        mixing.truncate()


if __name__ == "__main__":
    sort_papers_by_year("music_tech_papers - music_tech_papers.tsv")
    main("music_tech_papers - music_tech_papers.tsv")

    # find directory to put read me
    # write one readme.md for each paper
    # sort them by directory for them to be sit
    # export readme.md at the directory

'''
    args = [data_set1, source_code, demo1]
    print(args)
    for n, item in enumerate(args):
        if item == '':
            print("check", item)
            args[n] = "Not available"
    print("args", args)
    print("data_set1, source_code, demo1", data_set1, source_code, demo1)

    if source_code == '':
        source_code = "Not available"
    if demo1 == '':
        demo1 = "Not available"
        
        
# +'['+  +']' +'(' + + ')' +


'''
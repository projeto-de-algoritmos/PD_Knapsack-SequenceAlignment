import json 
from browser import (
    ajax,
    bind,
    document, 
    html
)


def addTask(evt):
    table = document.getElementById("task-table-body")
    newRow = document.createElement("tr")

    start = document.getElementById("start").value
    finish = document.getElementById("finish").value
    weight = document.getElementById("weight").value
    
    cell1 = document.createElement("th")
    cell2 = document.createElement("td")
    cell3 = document.createElement("td")
    cell4 = document.createElement("td")

    cell1.text = str(len(table.children))
    cell2.text = start
    cell3.text = finish
    cell4.text = weight

    newRow.appendChild(cell1)
    newRow.appendChild(cell2)
    newRow.appendChild(cell3)
    newRow.appendChild(cell4)

    table.appendChild(newRow)

def on_complete(req):
    data = json.loads(req.text)
    print(data.get('scheduled_tasks'))
    document['tasks'] <= html.P(data.get('scheduled_tasks'))
    document['t_weight'] <= html.SPAN(data.get('t_weight'))

def runScheduling(evt):
    table = document.getElementById('task-table')
    rows = table.getElementsByTagName('tr')

    data = []

    for i in range(1, len(rows)):
        cells = rows[i].getElementsByTagName('td')
        rowData = []
        for cell in cells:
            rowData.append(cell.text)
        data.append(rowData)

    table_data_str = ';'.join(','.join(row) for row in data)

    ajax.get(
        'runscheduling?tableData=' + table_data_str,
        oncomplete=on_complete,
    )   

document["runScheduling"].bind("click", runScheduling)
document["addBtn"].bind("click", addTask)
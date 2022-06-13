# var data = JSON.parse(jsondata);
# var ar = [];
# for (var i in data.data){
#     for (var k in data.data[i].values) {
#         ar.push([data.data[i].title, data.data[i].values[k].value]);
#     }
# }
# ass = SpreadsheetApp.getActiveSpreadsheet();
# ass.getRange('a1').offset(0, 0, ar.length, ar[0].length).setValues(ar);
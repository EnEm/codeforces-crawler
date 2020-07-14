let api_url = 'https://codeforces.com/api'
let handle = ''

let verdicts = {}
let langs = {}
let totalSub = 0
let handle = `${user}`

google.charts.load('current', {'packages':['corechart']})

google.charts.setOnLoadCallback(SubmissionsAccuracy)
google.charts.setOnLoadCallback(Languagesused)

function SubmissionsAccuracy(){
    // $.get(api_url+'user.status', {handle: handle}, function(data, status)
    // {
    //     console.log(data);
    // })
    console.log(handle)
}

function Languagesused(){

}


function drawCharts(){
    
}





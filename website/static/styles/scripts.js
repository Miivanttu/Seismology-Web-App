function selectArvutused(shown, hidden)
{
    var a = document.getElementById(shown);
    var b = document.getElementById(hidden);  
    a.style.display='block';
    b.style.display='none';
}
function selectParameter(shown, hidden)
{
    var a = document.getElementById(shown);
    var b = document.getElementById(hidden);  
    a.style.display='flex';
    b.style.display='none';
}
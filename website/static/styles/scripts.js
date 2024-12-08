function selectArvutused(shown, hidden)
{
    var a = document.getElementById(shown);
    var b = document.getElementById(hidden);  
    a.style.display='block';
    toggleRequired(a, true);
    b.style.display='none';
    toggleRequired(b, false);
}
function selectParameter(shown, hidden)
{
    var a = document.getElementById(shown);
    var b = document.getElementById(hidden);  
    a.style.display='flex';
    toggleRequired(a, true);
    b.style.display='none';
    toggleRequired(b, false);
}
function toggleRequired(element, isRequired) {
    // Find all input fields inside the given element
    var inputs = element.querySelectorAll('input');

    inputs.forEach(input => {
        if (isRequired) {
            input.setAttribute('required', 'required');
        } else {
            input.removeAttribute('required');
        }
    });
}
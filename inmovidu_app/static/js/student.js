function show_form(jobid,pos){
    document.getElementById("jobid").value=jobid;
    document.getElementById("position").value=pos
    console.log(pos)
    $("#student_apply_form").fadeIn(1500);
    document.getElementById("student_apply_form").style.display="flex";
    document.getElementById("allcards").style.display="none";
}
function jobs(){
    $("#allcards").fadeIn(1500);
    document.getElementById("allcards").style.display="flex";
    document.getElementById("student_apply_form").style.display="none";
}
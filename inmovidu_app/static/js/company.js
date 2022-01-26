function jobs_by_you(){
    $("#jobs_by_you").fadeIn(1500);
    document.getElementById("all_jobs").style.display="none";
    document.getElementById("new_job_form").style.display="none";
    document.getElementById("student_info").style.display="none";
}
function all_jobs(){
    $("#all_jobs").fadeIn(1500);
    document.getElementById("all_jobs").style.display="flex";
    document.getElementById("student_info").style.display="none";
    document.getElementById("jobs_by_you").style.display="none";
    document.getElementById("new_job_form").style.display="none";
}
function new_job_form(){
    $("#new_job_form").fadeIn(1500);
    document.getElementById("jobs_by_you").style.display="none";
    document.getElementById("student_info").style.display="none";
    document.getElementById("all_jobs").style.display="none";
}
function openinfo_student(){
    $("#student_info").fadeIn(1500);
    document.getElementById("jobs_by_you").style.display="none";
    document.getElementById("new_job_form").style.display="none";
    document.getElementById("all_jobs").style.display="none";
}
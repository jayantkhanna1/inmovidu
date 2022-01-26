function show_company_reg(){
    $("#form-3").fadeIn(1000);
    document.getElementById("form-1").style.display="none";
    document.getElementById("form-2").style.display="none";
    document.getElementById("form-4").style.display="none";
}
function show_company_login(){
    $("#form-1").fadeIn(1000);
    document.getElementById("form-2").style.display="none";
    document.getElementById("form-3").style.display="none";
    document.getElementById("form-4").style.display="none";
    document.getElementById("hire_students").style.backgroundColor="#f20091";
    document.getElementById("hire_students").style.border="2px solid #f20091";
    document.getElementById("get_a_job").style.background="linear-gradient(180deg,#0000 0,#fff3)";
    document.getElementById("get_a_job").style.border="2px solid white";

}
function show_student_reg(){
    $("#form-4").fadeIn(1000);
    document.getElementById("form-1").style.display="none";
    document.getElementById("form-2").style.display="none";
    document.getElementById("form-3").style.display="none";
}
function show_student_login(){
    $("#form-2").fadeIn(1000);
    document.getElementById("form-3").style.display="none";
    document.getElementById("form-1").style.display="none";
    document.getElementById("form-4").style.display="none";
    document.getElementById("get_a_job").style.backgroundColor="#f20091";
    document.getElementById("get_a_job").style.border="2px solid #f20091";
    document.getElementById("hire_students").style.background="linear-gradient(180deg,#0000 0,#fff3)";
    document.getElementById("hire_students").style.border="2px solid white";
}
var theory,credit,mark;
var internal;
var total;
var grade;
var total_marks=0;

for(var i=1;i<=8;i++){
    total_marks=0;

    for(var j=2;j<11;j++){
        credit=document.querySelector("#sem"+i+" tr:nth-child("+j+") td:nth-child(2)" );
        theory=document.querySelector("#sem"+i+" tr:nth-child("+j+") td:nth-child(4)" );
        internal=document.querySelector("#sem"+i+" tr:nth-child("+j+") td:nth-child(3)" );
        try{
            total=parseInt(theory.textContent)+parseInt(internal.textContent);
        }
        catch(err){
            break;
        }
        document
        .querySelector("#sem"+i+" tr:nth-child("+j+") td:nth-child(5)" )
        .textContent=total.toString();
        total_marks+=total;
        mark = parseInt(theory.textContent);
        if(parseFloat(credit.textContent)==1.0){
            total = total*2;
            mark = 50
        }
        if(mark<20 || parseInt(internal.textContent)<20){
            grade="F";
        }
        else if(total>=90){
            grade="S";
        }
        else if(total>=75){
            grade="A";
        }
        else if(total>=60){
            grade="B";
        }
        else if(total>=50){
            grade="C";
        }
        else if(total>=40){
            grade="D";
        }
        else {
            grade="F";
        }
        document
        .querySelector("#sem"+i+" tr:nth-child("+j+") td:nth-child(6)" )
        .textContent=grade.toString();
    }
    
}



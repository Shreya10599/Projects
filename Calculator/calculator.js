//JavaScript code for JavaScript Calculator Assignment

//Function to display numbers in the display box
function dis(val) 
         { 
             document.getElementById("result").value+=val 
         } 

//Function to solve eqations involving addition, subtraction, multiplication or division
function solve() 
         { 
             let x = document.getElementById("result").value 
             let y = eval(x) 
             document.getElementById("result").value = y 
         } 

//Function to clear things in the display box
function clr() 
         { 
             document.getElementById("result").value = "" 
         } 

//Function to provide sine value
function sin()
         {
              let v = document.getElementById("result").value
              var s = Math.sin(v)
              document.getElementById("result").value = s
         }

//Function to provide cosine value
function cos()
         {
              let v = document.getElementById("result").value
              var c = Math.cos(v)
              document.getElementById("result").value = c
         }

//Function to provide tangent value
function tan()
         {
              let v = document.getElementById("result").value
              var t = Math.tan(v)
              document.getElementById("result").value = t
         }

//Function to give percent of the number in the display box
function percentage()
         {
              let v = document.getElementById("result").value
              var p = v/100;
              document.getElementById("result").value = p
         }
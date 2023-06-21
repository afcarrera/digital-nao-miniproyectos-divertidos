let tool = "lapiz";

let size = 15;

let paint = Boolean(false);

let primary_color = "#000";

let secondary_color = "#fff";

window.onload = function(){

	'use strict';

	let c = document.createElement("canvas");

	let ctx = c.getContext("2d");



	c.setAttribute("width", window.innerWidth);

	c.setAttribute("height", window.innerHeight);



	document.body.appendChild(c);



	c.onmousedown = function (e){

		paint = true;

		if( tool == "lapiz" ){

			ctx.moveTo(e.pageX - c.offsetLeft, e.pageY - c.offsetTop);

		}

	}

	c.onmouseup = function(){

		paint = false;

		ctx.beginPath();

	}

	c.onmousemove = function(e){

		if (paint) {

			if (tool == "lapiz") {

				ctx.lineTo(e.pageX - c.offsetLeft, e.pageY - c.offsetTop);

				ctx.lineWidth = size;

				ctx.strokeStyle = primary_color;

				ctx.stroke();

			}

			else if(tool == "borrador"){

				ctx.beginPath();

				ctx.clearRect(e.pageX - c.offsetLeft, e.pageY - c.offsetTop,size,size);

			}

		}

	}

	c.onmouseout = function(){

		paint = false;

	};

}
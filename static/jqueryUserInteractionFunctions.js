var CURRENT_URL=window.location.origin;

$(document).ready(function() {

	$(".buttonReset").click(function(){
		 location.reload(true);
		 
	});


	$(".buttonPredict").click(function(){
	
			var address=CURRENT_URL+"/makePrediction"+addingParams();
			$.ajax({
								type:"GET",
								url: address,
								dataType: "json",
								beforeSend: function() { 
									console.log("Before sending request..");
								},
								cache:false
					}).done(function( data, textStatus, jqXHR ) {
									
						console.log("Answer arrived!");
						var winner=data['winner']
						$(".winner").text("");
						$(".winner").append("Team "+winner);
						
						$(".winner").removeClass("BlueWin");
						$(".winner").removeClass("RedWin");
						
						if (winner=="BLUE"){
							$(".winner").addClass("BlueWin");
						}
						if (winner=="RED"){
							$(".winner").addClass("RedWin");
						}

					}).fail(function(request, textStatus, error){
							console.log("Negative answer!");
					}).always(function(jqXHR, textStatus, errorThrown ) {
							console.log("End Ajax call..")
					 });
	});
	
	
	document.getElementById('uploadMatch').addEventListener('change', function() {
            var fr=new FileReader();
            fr.onload=function(){
                //document.getElementById('output').textContent=fr.result;
				console.log(fr.result);
				var csv=fr.result;
				var lines = csv.split('\n');
					// remove one line, starting at the first position
				lines.splice(0,1);
				// join the array back into a single string
				var newtext = lines.join('\n');
				
				var lines = newtext.split('\n');
				var row=lines[0];
				
				var elements=row.split(',');
				
//  -- 	section BLUE 10 MIN				
				$("#BLUE_CURR_GOLD_10").val(elements[2]);
				$("#BLUE_TOT_GOLD_10").val(elements[3]);
				$("#BLUE_LEVEL_10").val(elements[4]);
				$("#BLUE_TOT_MINIONS_10").val(elements[5]);
				$("#BLUE_TOTJNG_MINIONS_10").val(elements[6]);
				
				$("#BLUE_TOT_KILLS_10").val(elements[8]);
				$("#BLUE_TOT_DEATH_10").val(elements[9]);
				$("#BLUE_TOT_ASSIST_10").val(elements[10]);
				$("#BLUE_WARD_PLACED_10").val(elements[11]);
				$("#BLUE_WARD_DESTR_10").val(elements[12]);
				
				var blueFirstTower10= elements[13];
				if (blueFirstTower10=="0"){
					 $( "#BLUE_firstTower10_1" ).prop( "checked", false );
					 $( "#BLUE_firstTower10_0" ).prop( "checked", true );
				}
				if (blueFirstTower10=="1"){
					 $( "#BLUE_firstTower10_1" ).prop( "checked", true );
					 $( "#BLUE_firstTower10_0" ).prop( "checked", false );
				}
				
				$("#BLUE_towers_10").val(elements[16]);
				$("#BLUE_inhibitors_10").val(elements[17]);
				
				
				
				var blueFirstDragon10= elements[18];
				if (blueFirstDragon10=="0"){
					 $( "#BLUE_FIRST_DRAGON_10_1" ).prop( "checked", false );
					 $( "#BLUE_FIRST_DRAGON_10_0" ).prop( "checked", true );
				}
				if (blueFirstDragon10=="1"){
					 $( "#BLUE_FIRST_DRAGON_10_1" ).prop( "checked", true );
					 $( "#BLUE_FIRST_DRAGON_10_0" ).prop( "checked", false );
				}
				
				$("#BLUE_DRAGONS_10").val(elements[19]);
				$("#BLUE_HERALDS_10").val(elements[20]);
				
// -- section BLUE 15 MIN					

				$("#BLUE_CURR_GOLD_15").val(elements[21]);
				$("#BLUE_TOT_GOLD_15").val(elements[22]);
				$("#BLUE_LEVEL_15").val(elements[23]);
				$("#BLUE_TOT_MINIONS_15").val(elements[24]);
				$("#BLUE_TOTJNG_MINIONS_15").val(elements[25]);
				
				var blueFirstKill= elements[26];
				if (blueFirstKill=="0"){
					 $( "#BLUE_firstKill_1" ).prop( "checked", false );
					 $( "#BLUE_firstKill_0" ).prop( "checked", true );
				}
				if (blueFirstKill=="1"){
					 $( "#BLUE_firstKill_1" ).prop( "checked", true );
					 $( "#BLUE_firstKill_0" ).prop( "checked", false );
				}
				
				$("#BLUE_TOT_KILLS_15").val(elements[27]);
				$("#BLUE_TOT_DEATH_15").val(elements[28]);
				$("#BLUE_TOT_ASSIST_15").val(elements[29]);
				$("#BLUE_WARD_PLACED_15").val(elements[30]);
				$("#BLUE_WARD_DESTR_15").val(elements[31]);
				
				var blueFirstTower15= elements[32];
				if (blueFirstTower15=="0"){
					 $( "#BLUE_firstTower15_1" ).prop( "checked", false );
					 $( "#BLUE_firstTower15_0" ).prop( "checked", true );
				}
				if (blueFirstTower15=="1"){
					 $( "#BLUE_firstTower15_1" ).prop( "checked", true );
					 $( "#BLUE_firstTower15_0" ).prop( "checked", false );
				}
				
				var blueFirstInhibitor15= elements[33];
				if (blueFirstInhibitor15=="0"){
					 $( "#BLUE_firstInhibitor_1" ).prop( "checked", false );
					 $( "#BLUE_firstInhibitor_0" ).prop( "checked", true );
				}
				if (blueFirstInhibitor15=="1"){
					 $( "#BLUE_firstInhibitor_1" ).prop( "checked", true );
					 $( "#BLUE_firstInhibitor_0" ).prop( "checked", false );
				}
				
				$("#BLUE_firstTowerLane").val(elements[34]);
				
				$("#BLUE_towers_15").val(elements[35]);
				$("#BLUE_inhibitors_15").val(elements[36]);
				
				
				var blueFirstDragon15= elements[37];
				if (blueFirstDragon15=="0"){
					 $( "#BLUE_FIRST_DRAGON_15_1" ).prop( "checked", false );
					 $( "#BLUE_FIRST_DRAGON_15_0" ).prop( "checked", true );
				}
				if (blueFirstDragon15=="1"){
					 $( "#BLUE_FIRST_DRAGON_15_1" ).prop( "checked", true );
					 $( "#BLUE_FIRST_DRAGON_15_0" ).prop( "checked", false );
				}
				
				$("#BLUE_DRAGONS_15").val(elements[38]);
				$("#BLUE_HERALDS_15").val(elements[39]);
				
// -- section RED 10 MIN

				$("#RED_CURR_GOLD_10").val(elements[41]);
				$("#RED_TOT_GOLD_10").val(elements[42]);
				$("#RED_LEVEL_10").val(elements[43]);
				$("#RED_TOT_MINIONS_10").val(elements[44]);
				$("#RED_TOTJNG_MINIONS_10").val(elements[45]);
				
				$("#RED_TOT_KILLS_10").val(elements[47]);
				$("#RED_TOT_DEATH_10").val(elements[48]);
				$("#RED_TOT_ASSIST_10").val(elements[49]);
				$("#RED_WARD_PLACED_10").val(elements[50]);
				$("#RED_WARD_DESTR_10").val(elements[51]);
				
				var redFirstTower10= elements[52];
				if (redFirstTower10=="0"){
					 $( "#RED_firstTower10_1" ).prop( "checked", false );
					 $( "#RED_firstTower10_0" ).prop( "checked", true );
				}
				if (redFirstTower10=="1"){
					 $( "#RED_firstTower10_1" ).prop( "checked", true );
					 $( "#RED_firstTower10_0" ).prop( "checked", false );
				}
				
				$("#RED_towers_10").val(elements[55]);
				$("#RED_inhibitors_10").val(elements[56]);
				
				
				
				var redFirstDragon10= elements[57];
				if (redFirstDragon10=="0"){
					 $( "#RED_FIRST_DRAGON_10_1" ).prop( "checked", false );
					 $( "#RED_FIRST_DRAGON_10_0" ).prop( "checked", true );
				}
				if (redFirstDragon10=="1"){
					 $( "#RED_FIRST_DRAGON_10_1" ).prop( "checked", true );
					 $( "#RED_FIRST_DRAGON_10_0" ).prop( "checked", false );
				}
				
				$("#RED_DRAGONS_10").val(elements[58]);
				$("#RED_HERALDS_10").val(elements[59]);
				
// --section RED 15 MIN
				
				$("#RED_CURR_GOLD_15").val(elements[60]);
				$("#RED_TOT_GOLD_15").val(elements[61]);
				$("#RED_LEVEL_15").val(elements[62]);
				$("#RED_TOT_MINIONS_15").val(elements[63]);
				$("#RED_TOTJNG_MINIONS_15").val(elements[64]);
				
				var redFirstKill= elements[65];
				if (redFirstKill=="0"){
					 $( "#RED_firstKill_1" ).prop( "checked", false );
					 $( "#RED_firstKill_0" ).prop( "checked", true );
				}
				if (redFirstKill=="1"){
					 $( "#RED_firstKill_1" ).prop( "checked", true );
					 $( "#RED_firstKill_0" ).prop( "checked", false );
				}
				
				$("#RED_TOT_KILLS_15").val(elements[66]);
				$("#RED_TOT_DEATH_15").val(elements[67]);
				$("#RED_TOT_ASSIST_15").val(elements[68]);
				$("#RED_WARD_PLACED_15").val(elements[69]);
				$("#RED_WARD_DESTR_15").val(elements[70]);
				
				var redFirstTower15= elements[71];
				if (redFirstTower15=="0"){
					 $( "#RED_firstTower15_1" ).prop( "checked", false );
					 $( "#RED_firstTower15_0" ).prop( "checked", true );
				}
				if (redFirstTower15=="1"){
					 $( "#RED_firstTower15_1" ).prop( "checked", true );
					 $( "#RED_firstTower15_0" ).prop( "checked", false );
				}
				
				var redFirstInhibitor15= elements[72];
				if (redFirstInhibitor15=="0"){
					 $( "#RED_firstInhibitor_1" ).prop( "checked", false );
					 $( "#RED_firstInhibitor_0" ).prop( "checked", true );
				}
				if (redFirstInhibitor15=="1"){
					 $( "#RED_firstInhibitor_1" ).prop( "checked", true );
					 $( "#RED_firstInhibitor_0" ).prop( "checked", false );
				}
				
				$("#RED_firstTowerLane").val(elements[73]);
				
				$("#RED_towers_15").val(elements[74]);
				$("#RED_inhibitors_15").val(elements[75]);
				
				
				var redFirstDragon15= elements[76];
				if (redFirstDragon15=="0"){
					 $( "#RED_FIRST_DRAGON_15_1" ).prop( "checked", false );
					 $( "#RED_FIRST_DRAGON_15_0" ).prop( "checked", true );
				}
				if (blueFirstDragon15=="1"){
					 $( "#RED_FIRST_DRAGON_15_1" ).prop( "checked", true );
					 $( "#RED_FIRST_DRAGON_15_0" ).prop( "checked", false );
				}
				
				$("#RED_DRAGONS_15").val(elements[77]);
				$("#RED_HERALDS_15").val(elements[78]);
            } 
            fr.readAsText(this.files[0]);
	});
	
	
	function addingParams(){

			var returnParams="?";
			
			$(".mainTable :input").each(function( index ) {
				
				if ($(this).is('input:text')){
						returnParams+="&"+$(this).prop("id")+"="+$(this).prop("value");
				}
				if ($(this).is('select')){
						returnParams+="&"+$(this).prop("id")+"="+$(this).prop("value");
				}
				
				if ($(this).is('input:radio')){
						if ($(this).is('input:radio:checked')){
							returnParams+="&"+$(this).prop("name")+"="+$(this).prop("value");
						}
				}
			});

			return returnParams;
	}	
	
});

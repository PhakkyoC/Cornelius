$(function () {
    $('#my-calendar').datepicker({
        language: "fr"
    });
});
let maxetapes = 3;
let date;
function to_form(id) {
    let percent = (((100/maxetapes)*id));
    if (id>1)
    {
        if(id<maxetapes)
        {
            $('#form-'+(id-1)).hide();
            $('#form-'+id).show();
            $('#form-'+(id+1)).hide();
            $('#progress').css("width",""+percent+'%')
            if(id+1==maxetapes)
            {
                $('#btn-submit').show();
            }
            if (id==3)
            {
                loadCard();
            }
        }
    }
    else
    {
        $('#form-'+(id+1)).hide();
        $('#form-'+(id)).show();
        $('#progress').css("width",""+percent+'%')
    }
}

function showLastField(self) {
    if (self.value==1 )
    {
        $('#out').hide();
        $('#out-display').hide();
        maxetapes = 3;
        $('#btn-suivant-2').hide();
        $('#progress').css("width",'33%')
    }
    else if(self.value!=="" && self.value!==undefined)
    {
        $('#out').show();
        $('#out-display').show();
        maxetapes = 4;
        $('#btn-suivant-2').show();
        $('#progress').css("width",'25%')
    }
}

function update(self) {
    binddata(self);
    let id = self.id.substr(0,self.id.indexOf('-'));
    id = id+'-display';
    let value="";
    if(self.type=="select-one")
    {
        value = self.options[self.selectedIndex].text;
    }
    else
    {
        value = self.value;
    }
    $('#'+id).html(value);
}

function binddata(self)
{
    let id = self.id.substr(0,self.id.indexOf('-'));
    id = id+'-hidden';
    $('#'+id).val(self.value);
}

function loadCard() {
    $.ajax({
    url: '/getplace',
    data: {
      'placetype': $('#placetype-hidden').val()
    },
    dataType: 'json',
    success: function (data) {
        let html ="";
        $('#card-div').empty();
        for (let elem of data.results)
        {
            html="<div class='col-sm-4'>\n" +
                "   <div class='card' onclick='selectCard("+elem.id+",\""+elem.name+"\",\""+elem.img+"\")'>\n" +
                "       <img src='static/img/"+elem.img+"' class='img-card' alt='Avatar' style='width:100%;height: 100%;'>\n" +
                "       <div class='container-card'>\n" +
                "           <h4><b>"+elem.name+"</b></h4>\n" +
                "           <div class='row'>\n" +
                "               <div class='col-sm-4'>\n" +
                "                   <span>"+elem.desc+"</span>\n" +
                "               </div>\n" +
                "               <div class='col-sm-8'>\n";

                for (let j of [1,2,3,4,5])
                {
                    if (elem.rating>=j)
                    {
                        html+="<span class='fa fa-star checked'></span>\n";
                    }
                    else
                    {
                        html+="<span class='fa fa-star'></span>\n";
                    }
                }

                html+="                   <span>"+elem.nbvotes+" Avis</span>\n" +
                "               </div>\n" +
                "           </div>\n" +
                "           <div class='row'>\n";

                for (let i of[1,2,3])
                {
                    if (elem["tag"+i]!="")
                    {
                        html+=" <div class='col-sm-2'>\n" +
                                "<span class='tag label label-info tag-perso'>"+elem["tag"+i]+"</span>\n" +
                              " </div>\n"
                    }
                }

                html+="           </div>\n" +
                "       </div>\n" +
                "   </div>\n" +
                " </div>";
            $('#card-div').append(html);
        }
    }
  });
}

function selectCard(id,title,img) {
    $('#place-hidden').val(id);
    $('#card-recap').show();
    $('#img-recap').attr('src',"static/img/"+img);
    $('#title-recap').html("<b>"+title+"</b>")
}

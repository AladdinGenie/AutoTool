/**
 * Created by zhaolixiao on 2016/9/28.
 */
var result_img = {
    'pass': '通过',
    'fail': '不通过',
    'notRun': '未执行'
};


function update_result_img(){
    var value = $(this).attr('value');
    $(this).html('<img alt="'+ result_img[value]+'" src=static/'+value+'.png>');
}

function expand_detail(){
    var target = $($(this).attr("data-target"));
    if(target.hasClass("hide")){
        target.show();
        target.removeClass('hide');
    }else{
        target.hide();
        target.addClass('hide');
    }
}

function show_choice(){
    var id = $(this).attr('id');
    $('.test_case').show();
    $('.detail_info').parent().hide();
    $('.detail_info').parent().addClass('hide');
    switch(id){
        case 'show_not_run':
            $(".result").filter("[value!='notRun']").parent().hide();
            break;
        case 'show_pass':
            $(".result").filter("[value!='pass']").parent().hide();
            break;
        case 'show_fail':
            $(".result").filter("[value!='fail']").parent().hide();
            break;
        default:
            break;
    }
}

function show_count(){
    var count;
    switch($(this).attr('id')){
        case 'show_not_run':
            count = $(".result").filter("[value='notRun']").parent().length;
            $(this).text($(this).text()+"："+count+"条");
            break;
        case 'show_pass':
            count = $(".result").filter("[value='pass']").parent().length;
            $(this).text($(this).text()+"："+count+"条");
            break;
        case 'show_fail':
            count = $(".result").filter("[value='fail']").parent().length;
            $(this).text($(this).text()+"："+count+"条");
            break;
        case 'show_all':
            count = $('.test_case').length;
            $(this).text($(this).text()+"："+count+"条");
            break;
    }
}

function default_show_fail(){
    switch($(this).attr('value')){
        case 'pass':
            count = $(this).parent().hide();
            break;
        default:
            break;
    }
}

$(document).ready(function(){
    $("[data-toggle='expand']").click(expand_detail);
    $(".result").each(update_result_img);
    $('.choice').click(show_choice);
    $('.choice').each(show_count);
    $('.result').each(default_show_fail);
});

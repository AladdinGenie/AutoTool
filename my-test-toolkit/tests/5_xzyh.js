    /**
     * 新增10个系统用户.
     *
     */
var config = require('./config.json')


var randomName = require("chinese-random-name");

//生成从minNum到maxNum的随机数
function randomNum(minNum,maxNum){ 
    switch(arguments.length){ 
        case 1: 
            return parseInt(Math.random()*minNum+1,10); 
        break; 
        case 2: 
            return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
        break; 
            default: 
                return 0; 
            break; 
    } 
}

module.exports = {
  '新增系统用户测试': function (client) {
	const username ='#login-card-input-wrap > div:nth-child(1) > div > input'
	const password = '#login-card-input-wrap > div:nth-child(2) > div > input'
	const login_button = '//*[@id="login-card"]/form/div[2]/button[2]'
    const yhgl_title = '//*[@id="app-list"]/div/div[4]/div[1]'
    const xzyh_button = '//*[@id="app-container"]/div/form/div[3]/button[2]'
    const xzyh_title = '//*[@id="app-list"]/div/div[4]/div[2]/div[3]/div/div/div[2]/div/div'
    const xzxtyh_title ='/html/body/div[3]/div/h3/div'
    const yh_name = '//*[@id="module-modal"]/div[1]/div[1]/div/div/input'
    const yh_nc_name = '//*[@id="module-modal"]/div[1]/div[2]/div/div/input'
    const yh_passwd = '//*[@id="module-modal"]/div[2]/div/div/input'
    const ys_save_button = '/html/body/div[3]/div/div[2]/div/button[2]'
    const ys_query_button = '//*[@id="app-container"]/div/form/div[3]/button[1]'

    client.url(config.url).maximizeWindow()

    // Login.
    client.waitForElementVisible('#login-card', 2*config.sleep)
    client.frame(0)
    client.pause(2*config.sleep)
    client.setValue(username, config.username)
    client.setValue(password, config.password)
    client.useXpath().click(login_button)
    client.pause(3*config.sleep)
    // 系统用户列
    client.useXpath().click(yhgl_title)
    client.expect.element(xzyh_title).to.be.present
    client.pause(config.sleep)
    client.useXpath().click(xzyh_title)
    client.pause(config.sleep)

    for( var i = 1;i < config.for_num;i++){
        ysstring = i.toString()
        bhstring = '000'+i.toString()
        client.useXpath().click(xzyh_button)
        client.expect.element(xzxtyh_title).to.be.present
        client.pause(config.sleep)
        client.setValue(yh_name,'zb_'+ ysstring)
        client.setValue(yh_nc_name,randomName.generate())
        client.setValue(yh_passwd,config.password)
        client.pause(config.sleep)
		for (var j =1;j < randomNum(2,config.select_num*2+5);j++){
            random = randomNum(1,config.select_num*2+5)
            yh_qx_select_done = '//*[@id="module-modal"]/div[3]/div[2]/div['+random.toString()+']/label'
            client.useXpath().click(yh_qx_select_done)
            client.pause(2*config.sleep)
        }
     client.useXpath().click(ys_save_button)
     client.pause(config.sleep)
    }
    client.useXpath().click(ys_query_button)
    client.pause(2*config.sleep)
    client.saveScreenshot('reports/xzyh.png')
    client.end()
  }
}

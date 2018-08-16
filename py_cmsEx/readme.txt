________________________________________________________________________________________________________

py_cmsEx : 구조개선,요청 및 응답에 대한 사전/사후 처리, 쿠키 도입 , DB연결 및 종료 개선 처리
           API기능 추가(json기반) , 블루프린트(미정)
________________________________________________________________________________________________________

static : 정적 폴더, css,js image 파일 업로드 저장위치
        라우트 업이 url 자동부여
        http://ip:port/static/xxx.xx
        정적 폴더르 변경할 수 없는가 ? >> 가능하다!
________________________________________________________________________________________________________

templates : render_template()에서 사용하는 html파일이 위치한다

________________________________________________________________________________________________________

run.py : 프로그램 시작점 , 서버의 시작점 
________________________________________________________________________________________________________

session : 사이트에 로그인한 유저의 특정 정보를 저장하여 서버가 관리한다.
          세션이 유지되는 동안 로그인 한 것으로 간주된다.
          특정 페이지 접근만 허락한다.
          동시 접속이 크면 DB쪽에 저장하지만 대량 유저가 동접하는
          규모가 아니면 서버 메모리에 저장하여 관리한다!

_________________________________________________________________________________________________________

(반대 개념)
cookie : 유저 브라우저에 저장하는 정보 (ex.아이디 저장)
_________________________________________________________________________________________________________

파일 업로드 :  ~/bbs/upload >> GET방식  >> 폼
              ~/bbs/upload >> POST방식 >> 등록
              ~/bbs        >> GET방식  >> 등록된 글 리스트
 _________________________________________________________________________________________________________

 1) service > controller > __init__.py에 blueprint 정의 추가

 2) service > __init__.py에 blueprint 등록
    + from ... import bp_bbs
      app.register_blueprint(bp_bbs,url_prefix='/bbs')

 3) service > controller > bbs.py 생성
    service > __init__.py에 bbs import
    from service.controller import epl,user,bbs
 
 4) 테이블 생성 및 SQL 테스트
    -- 테이블 생성 SQL문
    CREATE TABLE `tbl_bbs` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(50) NULL DEFAULT NULL,
	`content` TEXT NULL DEFAULT NULL,
	`file` VARCHAR(512) NULL DEFAULT NULL,
	`writer` VARCHAR(50) NULL DEFAULT NULL,
	`regdate` TIMESTAMP NOT NULL DEFAULT '',
	PRIMARY KEY (`id`)   )

   -- 쿼리문
   -- 전체 게시물 가져오기

        select 
                *
        from 
                tbl_bbs
        order by id desc ;
                
        -- 게시물 하나 추가하기

        insert into tbl_bbs(title,content,`file`,writer)
        values('테스트2','또 테스트','/upload/img/test.png','Mira'); 

 5) service > model > dbMgr.py에 멤버함수 2개 추가 
    
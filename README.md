# 当前任务：

## 1.学生端的竞赛信息获取

用到的数据库：competition_upload_competition(储存了竞赛信息和独有id) \ competition_teacher_teacherinformation(通过独有id返回教师名字)

后端：完成teacher端的api ，competition端的api已完成（api/competition/list/）

前端：展示列表，前半展示竞赛信息，后半展示教师信息

## 2.学生端报名信息提交

用到的数据库：apply(未建)->数据包含信息：学生的user_id，学生信息，指导老师，审批状态

后端：接受报名信息存到数据库（未设计），设计api展示学生报名信息

前端：设计学生报名界面

## 3.教师审批学生报名信息

用到的数据库：apply

后端:通过前端设计的审批按钮改变数据库中的审批状态

前端：设计交互逻辑

## 4.学生接受报名反馈并上传材料

数据库：apply，competition_student_uploadedfile

后端：无

前端：交互逻辑

（上传疑似做完了)

## 5.教师端下载材料

数据库：competition_student_uploadedfile

## X.前端美化




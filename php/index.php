<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Sublime插件生成</title>
	<style>
		.form{
			/* auto; */
			text-align: center;
		}
		.form input[type="text"]{
			margin-top:10px;
			width:300px;
		}
		textarea{
			margin-top:10px;
			width:300px;
		}

		.form input[type="submit"]{
			margin-top:10px;
			width:80px;
			height:30px;
		}	

		.form lable{
			display:inline-block;
			width:80px;
			font-size:12px;
		}
	</style>
</head>
<body>
	
	<center>

		<h1 style="margin-top:100px;">Sublime插件生成</h1>

		<form action="" method="post" class="form">
			<lable>根目录</lable>
			<input type="text" name="root_path" value="<?= getPost('root_path'); ?>" placeholder="输出目录"> <br>
			<lable>目录</lable>
			<input type="text" name="base_path" value="<?= getPost('base_path')? getPost('base_path') : '/'; ?>"> <br>
			<lable>触发函数</lable>
			<input type="text" name="trigger" value="<?= getPost('trigger'); ?>"> <br>
			<lable>触发内容</lable>
			<textarea name="content" rows="8"><?= getPost('content'); ?></textarea> <br>
			<lable>内容描述</lable>
			<input type="text" name="desc" value="<?= getPost('desc'); ?>"> <br>
			<lable>应用类型</lable>
			<input type="text" name="scope" value="<?= getPost('scope')? getPost('scope') : 'source.php'; ?>"> <br>

			<input type="submit" value="生 成"> <br>
		</form>
	</center>


</body>
</html>

<?php
	if( isset( $_POST['trigger'] ) ){
		
		$root_path	= $_POST['root_path'];
		$base_path	= $_POST['base_path'];
		$trigger 	= $_POST['trigger'];
		$content	= $_POST['content'];
		$desc 		= $_POST['desc'];
		$scope		= $_POST['scope'];

		include 'plug.php';

		$plug = new Plug($root_path,$base_path);

		$plug->build($trigger,$content,$desc,$scope);

		echo '<center> <h1> 生成成功! </h1> </center>';
	}

	function getPost($key){
		if(isset($_POST[$key])){
			return $_POST[$key];
		}else{
			return '';
		}
	}
?>
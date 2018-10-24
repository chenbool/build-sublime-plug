<?php

class Plug
{
	protected $root_path;
	protected $base_path='/';

	function __construct($root_path,$base_path)
	{
		$this->root_path = $root_path;
		$this->base_path = $base_path;
	}

	public function build($trigger,$content,$desc,$scope='source.php')
	{
		$tpl = "<snippet>
	<content><![CDATA[${content}]]></content>
	<scope>${scope}</scope>
	<tabTrigger>${trigger}</tabTrigger>
	<description>${desc}</description>
</snippet>";
		$filename = str_replace(':','',trim(strtolower($trigger)) );
		$base_path = $this->root_path.$this->base_path;
		$filepath = $base_path.$filename.time().'.sublime-snippet';

		is_dir($this->root_path) || mkdir($this->root_path);
		is_dir($base_path) || mkdir($base_path);

		file_put_contents($filepath, $tpl );
	}

}



// $plug = new Plug('C:\\Users\\Administrator\\Desktop\\1','\\');

// $plug->build('where','where()','where查询');
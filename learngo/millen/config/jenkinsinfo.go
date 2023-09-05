package config

type JenkinsInfo struct {
	UserName   string `mapstructure:"username" json:"username" yaml:"username"`
	PassWord   string `mapstructure:"password" json:"password" yaml:"password"`
	JenkinsUrl string `mapstructure:"jenkinsurl" json:"jenkinsurl" yaml:"jenkinsurl"`
	JobName    string `mapstructure:"jobname" json:"jobname" yaml:"jobname"`
}

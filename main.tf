provider aws {
    region = var.region
    access_key = var.access_key
    secret_key = var.secret_key

}

resource "aws_security_group" "web-server-sg" {
    name = "web-server-sg"
    description = "allow incoming http connections"
    # allow port 80 for nginx
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    # allow to ssh in as user ubuntu with private key only ( NO PASSWORD AUTH!! )
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

}

resource aws_instance "web-server-vm" {
    ami = "ami-052efd3df9dad4825"  # 64 bit ubuntu 22.04
    instance_type = "t2.micro"
    key_name = "jeffmac_test_key"
    security_groups = ["${aws_security_group.web-server-sg.name}"]
    # bash shell script to run after spinning up VM
    user_data = <<-EOF
    #!/bin/bash
    sudo su
    apt update
    apt -y install openssh-server
    apt -y install python
    apt -y install curl
    apt -y install less
    apt -y install nginx
    apt -y install net-tools
    systemctl start ssh
    systemctl enable ssh

    systemctl start nginx
    systemctl enable nginx
    echo "<html><h1> Welcome to my little webserver </h1></html>" >> /var/www/html/index.html
    EOF
    tags = {
        name = "web_instance"
    }

}

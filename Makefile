##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## Makefile python
##

NAME =	mypgp

name:
	cp ${NAME}.py ${NAME}
	chmod 755 ${NAME}

clean:
	rm -f *~

fclean:	clean
	rm -f $(NAME)

re:	fclean	all

all:	name

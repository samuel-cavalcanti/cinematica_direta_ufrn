import sympy
from sympy import Symbol, Matrix, pi,Rational

TO_README =True

def from_joinTransform(a:Symbol,alpha:Symbol,d:Symbol,theta:Symbol)->sympy.Matrix:

    cos_theta = sympy.cos(theta)
    sen_theta = sympy.sin(theta)

    cos_alpha = sympy.cos(alpha)
    sen_alpha = sympy.sin(alpha)
    

    matrix  = [[0]*4 for _ in range(4)]

    matrix[0][0] = cos_theta

    matrix[0][1] = -sen_theta

    matrix[0][2] = 0

    matrix[0][3] = a

    matrix[1][0] = cos_alpha*sen_theta

    matrix[1][1] = cos_alpha*cos_theta

    matrix[1][2] = -sen_alpha

    matrix[1][3] = -sen_alpha * d

    matrix[2][0] = sen_alpha * sen_theta
    matrix[2][1] = sen_alpha * cos_theta
    matrix[2][2] = cos_alpha
    matrix[2][3] = cos_alpha * d

    for i in range(4):
        matrix[3][i] =0
 
    matrix[-1][-1] = 1

    return Matrix(matrix)


def from_degree(degree:int)-> float:
    """

         180 == pi
          x  == y
          x*pi/180

    """
    return pi*Rational(degree,180)


def print_readme_latex(matrix,title:str):
    
    latex:str = str(sympy.latex(matrix))
    latex = latex.replace("\\\\","\\\\ \n")
    latex = latex.replace("\left[\\begin{matrix}","\left[\\begin{matrix}\n")
    latex =latex.replace("\end{matrix}\\right]","\n\end{matrix}\\right]")
    output_string = \
f"""
## {title} 
        
$$
{latex}
$$

"""
    
    print(output_string)

def main():

   
    sympy.init_printing(use_unicode=True)
 
    matrix_1 = from_joinTransform(
        a=0,
        alpha=0,
        d=Symbol('h'),
        theta=Symbol('theta_1')
    )

    matrix_2 = from_joinTransform(
        a=Symbol('L_1'),
        alpha=0,
        d=Symbol('d_2'),
        theta=0
    )

    matrix_3 = from_joinTransform(
        a=0,
        alpha=from_degree(90),
        d=0,
        theta=Symbol('theta_3')
    )

    matrix_4 = from_joinTransform(
        a=Symbol('L_2'),
        alpha=from_degree(0),
        d=0,
        theta=from_degree(0)
    )

    result = ((matrix_1 * matrix_2) * matrix_3) * matrix_4


    


    def pprint(matrix,title:str):
        print(title,end='\n\n')
        sympy.pprint(matrix)
        print()

    if TO_README:
        print_readme_latex(matrix_1,"Matrix $0_{T_1}$")
        print_readme_latex(matrix_2,"Matrix $1_{T_2}$")
        print_readme_latex(matrix_3,"Matrix $2_{T_3}$")
        print_readme_latex(matrix_4,"Matrix $3_{T_4}$")
        print_readme_latex(result,"Matrix $0_{T_4}$")
    else:
        pprint(matrix_1,'Matrix 1')
        pprint(matrix_2,'Matrix 2')
        pprint(matrix_3,'Matrix 3')
        pprint(matrix_4,'Matrix 4')

        pprint(result,'Result')
    
    


if __name__ == '__main__':
    main()

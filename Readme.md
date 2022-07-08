# cinemática direta de um manipulador robótico

calculo da cinemática de  braço robótico


![braço](docs/exemplo_braco.png)

[exercicio_braço_robotico.pdf](docs/Avaliao_Semanal_sobre_cinemtica_direta.pdf)


| $i$ | $a_{i-1}$ | $\alpha_{i-1}$ | $d_{i}$ | $\theta_i$ |
| --- | --------- | -------------- | ------- | ---------- |
| 1   | $0$       | $0$            | $h$     | $\theta_1$ |
| 2   | $L_1$     | $0$            | $d_2$   | $0$        |
| 3   | $0$       | $90$           | $0$     | $\theta_3$ |
| 4   | $L_2$     | $0$            | $0$     | $0$        |

 
```python
# elo_transform_sympy.py
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
```

```zsh
python3 elo_transform_sympy.py

Matrix 1

⎡cos(θ₁)  -sin(θ₁)  0  0⎤
⎢                       ⎥
⎢sin(θ₁)  cos(θ₁)   0  0⎥
⎢                       ⎥
⎢   0        0      1  h⎥
⎢                       ⎥
⎣   0        0      0  1⎦

Matrix 2

⎡1  0  0  L₁⎤
⎢           ⎥
⎢0  1  0  0 ⎥
⎢           ⎥
⎢0  0  1  d₂⎥
⎢           ⎥
⎣0  0  0  1 ⎦

Matrix 3

⎡cos(θ₃)  -sin(θ₃)  0   0⎤
⎢                        ⎥
⎢   0        0      -1  0⎥
⎢                        ⎥
⎢sin(θ₃)  cos(θ₃)   0   0⎥
⎢                        ⎥
⎣   0        0      0   1⎦

Matrix 4

⎡1  0  0  L₂⎤
⎢           ⎥
⎢0  1  0  0 ⎥
⎢           ⎥
⎢0  0  1  0 ⎥
⎢           ⎥
⎣0  0  0  1 ⎦

Result

⎡cos(θ₁)⋅cos(θ₃)  -sin(θ₃)⋅cos(θ₁)  sin(θ₁)   L₁⋅cos(θ₁) + L₂⋅cos(θ₁)⋅cos(θ₃)  ⎤
⎢                                                                            ⎥
⎢sin(θ₁)⋅cos(θ₃)  -sin(θ₁)⋅sin(θ₃)  -cos(θ₁)  L₁⋅sin(θ₁) + L₂⋅sin(θ₁)⋅cos(θ₃)  ⎥
⎢                                                                            ⎥
⎢    sin(θ₃)          cos(θ₃)          0            L₂⋅sin(θ₃) + d₂ + h      ⎥
⎢                                                                            ⎥
⎣       0                0             0                     1               ⎦

```
##  Matriz $0_{T_1}$

$$
\left[\begin{matrix}
\cos{\left(\theta_{1} \right)} & - \sin{\left(\theta_{1} \right)} & 0 & 0 \\
\sin{\left(\theta_{1} \right)} & \cos{\left(\theta_{1} \right)} & 0 & 0 \\
0 & 0 & 1 & h\\
0 & 0 & 0 & 1
\end{matrix}\right]
$$

##  Matriz $1_{T_2}$

$$
\left[\begin{matrix}1 & 0 & 0 & L_{1}\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & d_{2}\\
0 & 0 & 0 & 1
\end{matrix}\right]
$$

##  Matriz $2_{T_3}$

$$
\left[\begin{matrix}
\cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{3} \right)} & 0 & 0\\
0 & 0 & -1 & 0\\
\sin{\left(\theta_{3} \right)} & \cos{\left(\theta_{3} \right)} & 0 & 0\\
0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $3_{T_4}$

$$
\left[\begin{matrix}
1 & 0 & 0 & L_{2}\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{matrix}\right]
$$

##  Matriz $0_{T_4}$

$$
\left[\begin{matrix}
\cos{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{3} \right)} \cos{\left(\theta_{1} \right)} & \sin{\left(\theta_{1} \right)} & L_{1} \cos{\left(\theta_{1} \right)} + L_{2} \cos{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)}\\
\sin{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{1} \right)} \sin{\left(\theta_{3} \right)} & - \cos{\left(\theta_{1} \right)} & L_{1} \sin{\left(\theta_{1} \right)} + L_{2} \sin{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)}\\
\sin{\left(\theta_{3} \right)} & \cos{\left(\theta_{3} \right)} & 0 & L_{2} \sin{\left(\theta_{3} \right)} + d_{2} + h\\0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $0_{T_1}$

$$
\left[\begin{matrix}\cos{\left(\theta_{1} \right)} & - \sin{\left(\theta_{1} \right)} & 0 & 0\\
\sin{\left(\theta_{1} \right)} & \cos{\left(\theta_{1} \right)} & 0 & 0\\0 & 0 & 1 & h\\0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $1_{T_2}$

$$
\left[\begin{matrix}1 & 0 & 0 & L_{1}\\0 & 1 & 0 & 0\\0 & 0 & 1 & d_{2}\\0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $2_{T_3}$

$$
\left[\begin{matrix}\cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{3} \right)} & 0 & 0\\0 & 0 & -1 & 0\\
\sin{\left(\theta_{3} \right)} & \cos{\left(\theta_{3} \right)} & 0 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $3_{T_4}$

$$
\left[\begin{matrix}1 & 0 & 0 & L_{2}\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{matrix}\right]
$$

##  Matriz $0_{T_4}$

$$
\left[\begin{matrix}\cos{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{3} \right)} \cos{\left(\theta_{1} \right)} & \sin{\left(\theta_{1} \right)} & L_{1} \cos{\left(\theta_{1} \right)} + L_{2} \cos{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)}\\
\sin{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)} & - \sin{\left(\theta_{1} \right)} \sin{\left(\theta_{3} \right)} & - \cos{\left(\theta_{1} \right)} & L_{1} \sin{\left(\theta_{1} \right)} + L_{2} \sin{\left(\theta_{1} \right)} \cos{\left(\theta_{3} \right)}\\
\sin{\left(\theta_{3} \right)} & \cos{\left(\theta_{3} \right)} & 0 & L_{2} \sin{\left(\theta_{3} \right)} + d_{2} + h\\0 & 0 & 0 & 1\end{matrix}\right]
$$

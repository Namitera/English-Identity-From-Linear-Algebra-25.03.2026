from manim import *

class Thumbnail(ThreeDScene):
    def construct(self):

        a = Tex("Identity from").scale(2).shift(UP*2).set_z_index(2)
        b = Tex("Linear algebra").scale(2).next_to(a,DOWN).align_to(a,LEFT).set_z_index(2)
        b1 = SurroundingRectangle(b, fill_opacity=0.9, fill_color=BLACK, stroke_opacity=0).set_z_index(1)
        b2 = SurroundingRectangle(a, fill_opacity=0.9, fill_color=BLACK, stroke_opacity=0).set_z_index(1)

        self.add_fixed_in_frame_mobjects(b1,b2,a,b)

        v1 = Vector([3,0], color=RED)        
        v2 = Vector([0,3], color=GREEN)
        v3 = Vector([3,0], color=BLUE).rotate_about_origin(-PI/2, UP)
        att1 = Tex("rationality").next_to(v1,DOWN).set_color(RED)
        att2 = Tex("emotionality").shift(LEFT*0.6+UP*1.5).set_color(GREEN).rotate(PI/2)
        att3 = Tex("analyticity").set_color(BLUE).rotate(PI/2).rotate(PI/2, UP).next_to(v3, DOWN)

        #build
        self.play(Create(v1))
        self.play(Create(v2))
        self.play(Write(att1))
        self.play(Write(att2))
        self.play(Create(v3))
        self.play(Write(att3))

        #persons in space
        p1 = Vector([2,1,1])
        p2 = Vector([2,1,1]).rotate_about_origin(PI/2, [2,1,1])
        p1tex = MathTex(r"P_{1}=\begin{bmatrix}1\cdot rationality\\1\cdot emotionality\\1\cdot analyticity\end{bmatrix}").to_corner(UL)
        p1tex[0][7:18].set_color(RED)
        p1tex[0][20:32].set_color(GREEN)
        p1tex[0][34:45].set_color(BLUE)
        b1 = SurroundingRectangle(p1tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.play(GrowArrow(p1),GrowArrow(p2))

        #second person
        p3 = Vector([0,2,2])
        p4 = Vector([0,2,2]).rotate_about_origin(PI/2, [0,2,2])
        p2tex = MathTex(r"finding \, \, a \, \, differnt \, \, person:",r"P_{1} \times P_{2}").to_corner(UL)
        p2tex[1].set_color(PURE_MAGENTA)
        b2 = SurroundingRectangle(p2tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.play(GrowArrow(p3),GrowArrow(p4))
        #new person
        p5 = Vector([0,-2,2]).set_color(PURE_MAGENTA)
        p6 = Vector([0,-2,2]).rotate_about_origin(PI/2, [0,-2,2]).set_color(PURE_MAGENTA)

        self.play(GrowArrow(p5),GrowArrow(p6))
        self.move_camera(zoom=2, frame_center=[1.5,0.5,1], theta=-1, phi=60*DEGREES)

class Contents(ThreeDScene):
    def construct(self):

        a = Tex("1. define what identity is").scale(1.2).to_corner(UL).set_z_index(2)
        b = Tex("2. how can it be changed").scale(1.2).next_to(a,DOWN).align_to(a,LEFT).set_z_index(2)
        c = Tex("3. measurements and correlation of identity").scale(1.2).next_to(b,DOWN).align_to(b,LEFT).set_z_index(2)
        b1 = SurroundingRectangle(b, fill_opacity=0.9, fill_color=BLACK, stroke_opacity=0).set_z_index(1)
        b2 = SurroundingRectangle(a, fill_opacity=0.9, fill_color=BLACK, stroke_opacity=0).set_z_index(1)
        b3 = SurroundingRectangle(c, fill_opacity=0.9, fill_color=BLACK, stroke_opacity=0).set_z_index(1)

        self.add_fixed_in_frame_mobjects(b1,b2,b3,a,b,c)

        v1 = Vector([3,0], color=RED)        
        v2 = Vector([0,3], color=GREEN)
        v3 = Vector([3,0], color=BLUE).rotate_about_origin(-PI/2, UP)
        att1 = Tex("rationality").next_to(v1,DOWN).set_color(RED)
        att2 = Tex("emotionality").shift(LEFT*0.6+UP*1.5).set_color(GREEN).rotate(PI/2)
        att3 = Tex("analyticity").set_color(BLUE).rotate(PI/2).rotate(PI/2, UP).next_to(v3, DOWN)

        #build
        self.play(Create(v1))
        self.play(Create(v2))
        self.play(Write(att1))
        self.play(Write(att2))
        self.play(Create(v3))
        self.play(Write(att3))

        #persons in space
        p1 = Vector([2,1,1])
        p2 = Vector([2,1,1]).rotate_about_origin(PI/2, [2,1,1])
        p1tex = MathTex(r"P_{1}=\begin{bmatrix}1\cdot rationality\\1\cdot emotionality\\1\cdot analyticity\end{bmatrix}").to_corner(UL)
        p1tex[0][7:18].set_color(RED)
        p1tex[0][20:32].set_color(GREEN)
        p1tex[0][34:45].set_color(BLUE)
        b1 = SurroundingRectangle(p1tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.play(GrowArrow(p1),GrowArrow(p2))

        #second person
        p3 = Vector([0,2,2])
        p4 = Vector([0,2,2]).rotate_about_origin(PI/2, [0,2,2])
        p2tex = MathTex(r"finding \, \, a \, \, differnt \, \, person:",r"P_{1} \times P_{2}").to_corner(UL)
        p2tex[1].set_color(PURE_MAGENTA)
        b2 = SurroundingRectangle(p2tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.play(GrowArrow(p3),GrowArrow(p4))
        #new person
        p5 = Vector([0,-2,2]).set_color(PURE_MAGENTA)
        p6 = Vector([0,-2,2]).rotate_about_origin(PI/2, [0,-2,2]).set_color(PURE_MAGENTA)

        self.play(GrowArrow(p5),GrowArrow(p6))
        self.move_camera(zoom=2, frame_center=[1.5,0.5,1], theta=-1, phi=60*DEGREES)

class DefineSpace(Scene):
    def construct(self):

        numLine = NumberLine(include_tip=True, x_range=[-6,6], length=13)
        numLine2 = NumberLine(include_tip=True, x_range=[-6,6], length=13).shift(UP*2)
        numLine3 = NumberLine(include_tip=True, length=7, x_range=[-6*7/13,6*7/13]).rotate(PI/2)
        att1 = Tex("rationality").to_edge(RIGHT).shift(DOWN)
        att2 = Tex("emotionality").to_edge(RIGHT).shift(UP*3)
        p1 = Dot(color=PURE_YELLOW).scale(2)
        p2 = Dot(color=PURE_YELLOW).scale(2).shift(UP*2)
        p3 = Dot(color=PURE_MAGENTA).scale(2)

        #first attribute
        self.wait()
        self.play(Write(numLine))
        self.wait()
        self.play(Write(att1))
        self.wait(3)
        self.play(Write(p1))
        self.wait(5)
        self.play(p1.animate.move_to([2,0,0]), run_time=2)
        self.play(p1.animate.move_to([-2,0,0]), run_time=2)
        self.play(p1.animate.move_to([0,0,0]), run_time=2)

        #snd attribute
        self.play(Write(numLine2))
        self.wait()
        self.play(Write(att2))
        self.wait()
        self.play(Write(p2))
        self.wait(3)

        self.play(p2.animate.move_to([2,2,0]), run_time=3)
        self.play(p2.animate.move_to([-2,2,0]), run_time=2)
        self.play(p2.animate.move_to([0,2,0]), run_time=3)

        #mix into 2d
        self.wait(3)
        self.play(FadeOut(p2))
        self.wait(2)
        self.play(Transform(numLine2,numLine3), att2.animate.shift(LEFT*3), run_time=4)
        self.wait(2)
        self.play(p1.animate.move_to([2,0,0]))
        self.wait()
        self.play(p1.animate.move_to([0,2,0]))
        self.wait()
        self.play(p1.animate.move_to([1,1,0]))
        self.play(p1.animate.move_to([-2,-1,0]))
        self.play(p1.animate.move_to([3,-2,0]))
        self.wait()

        self.play(Write(p3))
        self.play(p3.animate.move_to([-2,0,0]))
        self.play(p3.animate.move_to([1,1.5,0]))
        self.play(p3.animate.move_to([-3,2,0]))

        #more people
        p4 = Dot(color=PURE_RED).scale(2).move_to([2.5,1.3,0])
        p5 = Dot(color=PURE_GREEN).scale(2).move_to([-2.5,-1.3,0])
        p6 = Dot(color=PURE_BLUE).scale(2).move_to([0.6,1.9,0])
        p7 = Dot(color=ORANGE).scale(2).move_to([-0.6,-1.9,0])

        self.wait(3)
        self.play(Write(p4))
        self.play(Write(p5))
        self.play(Write(p6))
        self.play(Write(p7))
        self.wait(4)

        #transition to vectors
        v1 = Vector(p1.get_center(), color=p1.get_color())
        v3 = Vector(p3.get_center(), color=p3.get_color())
        v4 = Vector(p4.get_center(), color=p4.get_color())
        v5 = Vector(p5.get_center(), color=p5.get_color())
        v6 = Vector(p6.get_center(), color=p6.get_color())
        v7 = Vector(p7.get_center(), color=p7.get_color())

        self.play(GrowArrow(v1), FadeOut(p1))
        self.play(GrowArrow(v3), FadeOut(p3))
        self.play(GrowArrow(v4), FadeOut(p4))
        self.play(GrowArrow(v5), FadeOut(p5))
        self.play(GrowArrow(v6), FadeOut(p6))
        self.play(GrowArrow(v7), FadeOut(p7))
        self.wait()

class VectorPlane(Scene):
    def construct(self):
        
        num1 = NumberPlane().set_opacity(0.5)
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)
        att1 = Tex("rationality").next_to(ihatvec,DOWN).set_color(RED)
        att2 = Tex("emotionality").next_to(jhatvec,LEFT).set_color(GREEN)

        #build
        self.wait()
        self.play(Write(num1))
        self.play(GrowArrow(ihatvec))
        self.play(Write(att1))
        self.wait(9)
        self.play(GrowArrow(jhatvec))
        self.play(Write(att2))
        self.wait(9)

        #vector as person notation
        vec1 = num1.get_vector([1,2], color=PURE_YELLOW)
        vec2 = num1.get_vector([-5,-1], color=PURE_MAGENTA)
        p1 = MathTex(r"P_{1}=\begin{bmatrix}1\cdot rationality\\2\cdot emotionality\end{bmatrix}").move_to([3,3,0])
        p2 = MathTex(r"P_{2}=\begin{bmatrix}-5\cdot rationality\\-1\cdot emotionality\end{bmatrix}").move_to([-2,-2,0])
        p1[0][0:2].set_color(PURE_YELLOW)
        p1[0][6:17].set_color(RED)
        p1[0][19:31].set_color(GREEN)
        p2[0][0:2].set_color(PURE_MAGENTA)
        p2[0][7:18].set_color(RED)
        p2[0][21:33].set_color(GREEN)

        self.play(GrowArrow(vec1), run_time=3)
        self.wait(3)
        self.play(Write((p1)))
        self.wait(6)
        self.play(GrowArrow(vec2))
        self.play(Write((p2)))
        self.wait()

class VectorCompostion(Scene):
    def construct(self):

        num1 = NumberPlane().set_opacity(0.5)
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)
        att1 = Tex("rationality").next_to(ihatvec,DOWN).set_color(RED)
        att2 = Tex("emotionality").next_to(jhatvec,LEFT).set_color(GREEN)

        #build
        self.wait()
        self.play(Write(num1))
        self.play(GrowArrow(ihatvec))
        self.play(Write(att1))
        self.play(GrowArrow(jhatvec))
        self.play(Write(att2))
        self.wait(5)

        #vector as person notation
        vec1 = num1.get_vector([2,2], color=PURE_YELLOW)
        vec1b = num1.get_vector([0.5,0.5], color=PURE_YELLOW, stroke_width=112, max_stroke_width_to_length_ratio=11)
        vec2 = num1.get_vector([3,1], color=PURE_MAGENTA)
        vec2b = num1.get_vector([0.75,0.25], color=PURE_MAGENTA, stroke_width=112, max_stroke_width_to_length_ratio=11)
        p1 = MathTex(r"P_{1}=\begin{bmatrix}2\cdot rationality\\2\cdot emotionality\end{bmatrix}").move_to([3,3,0])
        p2 = MathTex(r"P_{2}=\begin{bmatrix}3\cdot rationality\\1\cdot emotionality\end{bmatrix}").move_to([3,-3,0])
        p1[0][0:2].set_color(PURE_YELLOW)
        p1[0][6:17].set_color(RED)
        p1[0][19:31].set_color(GREEN)
        p2[0][0:2].set_color(PURE_MAGENTA)
        p2[0][6:17].set_color(RED)
        p2[0][19:31].set_color(GREEN)

        p1hat = MathTex(r"\hat{P}_{1}=\begin{bmatrix}50 \% \cdot rationality\\50 \% \cdot emotionality\end{bmatrix}").to_corner(UL)
        p1hat[0][5:8].set_color(PURE_YELLOW)
        p1hat[0][20:23].set_color(PURE_YELLOW)
        p2hat = MathTex(r"\hat{P}_{2}=\begin{bmatrix}75 \% \cdot rationality\\25 \% \cdot emotionality\end{bmatrix}").to_corner(DL)
        p2hat[0][5:8].set_color(PURE_YELLOW)
        p2hat[0][20:23].set_color(PURE_YELLOW)

        determer = Square(side_length=np.sqrt(2), color=PURE_RED).rotate(PI/4)

        #first
        self.play(GrowArrow(vec1), run_time=2)
        self.wait()
        self.play(Write((p1)), run_time=2)
        self.wait(5)
        self.play(Unwrite(att1), Unwrite(att2))
        self.play(Write(determer))
        self.wait(9)
        self.play(vec1.animate.set_color(WHITE))
        self.play(ReplacementTransform(vec1.copy(), vec1b), run_time=3)
        self.wait()
        self.play(Write(p1hat))
        self.wait()

        #naming
        name = Tex("Identity composition").to_edge(LEFT).shift(UP*0.5)
        self.play(Write(name))
        self.wait(12)

        #second
        self.play(Unwrite(vec1b))
        self.play(GrowArrow(vec2))
        self.play(Write((p2)))
        self.wait(4)
        self.play(vec2.animate.set_color(WHITE))
        self.play(ReplacementTransform(vec2.copy(), vec2b), run_time=3)
        self.wait()
        self.play(Write(p2hat))
        self.wait(7)

        #clear and magnitude
        name2 = Tex("Identity magnitude").to_edge(LEFT).shift(UP*0.5)
        p1m = MathTex(r"|P_{1}|=2.83").to_corner(UL)
        p2m = MathTex(r"|P_{2}|=3.16").to_corner(DL)
        p1m[0][1:3].set_color(PURE_YELLOW)
        p2m[0][1:3].set_color(PURE_MAGENTA)

        self.play(vec1.animate.set_color(PURE_YELLOW), vec2.animate.set_color(PURE_MAGENTA))
        self.wait()
        self.play(Unwrite(VGroup(p1hat,p2hat,vec2b,name)))
        self.wait()
        self.play(Write(p1m))
        self.wait(7)
        self.play(Write(name2))
        self.wait()
        self.play(Write(p2m))
        self.wait()

class HigherDimensions(ThreeDScene):
    def construct(self):

        v1 = Vector([3,0], color=RED)        
        v2 = Vector([0,3], color=GREEN)
        v3 = Vector([3,0], color=BLUE).rotate_about_origin(-PI/2, UP)
        att1 = Tex("rationality").next_to(v1,DOWN).set_color(RED)
        att2 = Tex("emotionality").shift(LEFT*0.6+UP*1.5).set_color(GREEN).rotate(PI/2)
        att3 = Tex("analyticity").set_color(BLUE).rotate(PI/2).rotate(PI/2, UP).next_to(v3, DOWN)

        #build
        self.move_camera(phi=60*DEGREES, zoom=1.5, frame_center=[0,0,1])
        self.begin_ambient_camera_rotation(0.08)
        self.play(Create(v1))
        self.play(Create(v2))
        self.play(Write(att1))
        self.play(Write(att2))
        self.wait(3)
        self.play(Create(v3))
        self.wait(1)
        self.play(Write(att3))
        self.wait(4)

        #persons in space
        p1 = Vector([3,3,3])
        p2 = Vector([3,3,3]).rotate_about_origin(PI/2, [1,1,1])
        p1tex = MathTex(r"P_{1}=\begin{bmatrix}1\cdot rationality\\1\cdot emotionality\\1\cdot analyticity\end{bmatrix}").to_corner(UL)
        p1tex[0][7:18].set_color(RED)
        p1tex[0][20:32].set_color(GREEN)
        p1tex[0][34:45].set_color(BLUE)
        b1 = SurroundingRectangle(p1tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.move_camera(zoom=1, frame_center=[0,0,1])
        self.play(GrowArrow(p1),GrowArrow(p2), run_time=3)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(b1,p1tex)
        self.play(FadeIn(b1),Write(p1tex), run_time=2)

        #second person
        p3 = Vector([-2,-1,0])
        p4 = Vector([-2,-1,0]).rotate_about_origin(PI/2, [-2,-1,0])
        p2tex = MathTex(r"P_{2}=\begin{bmatrix}-2\cdot rationality\\-1\cdot emotionality\\0\cdot analyticity\end{bmatrix}").to_corner(UR)
        p2tex[0][8:19].set_color(RED)
        p2tex[0][22:34].set_color(GREEN)
        p2tex[0][36:47].set_color(BLUE)
        b2 = SurroundingRectangle(p2tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.wait(3)
        self.play(GrowArrow(p3),GrowArrow(p4))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(b2,p2tex)
        self.play(FadeIn(b2),Write(p2tex))
        self.wait(20)

class ScalarMultiplication(Scene):
    def construct(self):

        num1 = NumberPlane().set_opacity(0.5)
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)
        att1 = Tex("confidence").next_to(ihatvec,DOWN).set_color(RED)
        att2 = Tex("self-awareness").next_to(jhatvec,LEFT).set_color(GREEN)

        #build
        self.wait()
        self.play(Write(num1))
        self.play(GrowArrow(ihatvec))
        self.play(Write(att1))
        self.play(GrowArrow(jhatvec))
        self.play(Write(att2))
        self.wait(7)

        #original vector
        vec1 = num1.get_vector([2,1], color=PURE_YELLOW)
        p1 = MathTex(r"P_{1}=\begin{bmatrix}2\cdot confidence\\1\cdot self-awareness\end{bmatrix}").to_corner(UL)
        p1[0][0:2].set_color(PURE_YELLOW)
        p1[0][6:16].set_color(RED)
        p1[0][18:32].set_color(GREEN)

        self.play(GrowArrow(vec1), run_time=2)
        self.wait()
        self.play(Write(p1), run_time=2)

        #multiplication
        scalar = 2
        vec2 = num1.get_vector([scalar*2, scalar*1], color=PURE_YELLOW)
        p2 = MathTex(r"2(repeated \, success) \cdot",r"P_{1}=",r"\begin{bmatrix}2\cdot 2\cdot confidence\\2 \cdot 1\cdot self-awareness\end{bmatrix}").to_corner(UL)
        p2[1][0:2].set_color(PURE_YELLOW)
        p2[2][5:15].set_color(RED)
        p2[2][19:33].set_color(GREEN)

        self.wait(3)
        self.play(ReplacementTransform(vec1, vec2),run_time=3)
        self.wait(2)
        self.play(TransformMatchingShapes(p1, p2), run_time=3)
        self.wait(15)

        #backtransform
        p3 = MathTex(r"0.5(failure) \cdot",r"P_{1}=",r"\begin{bmatrix}0.5\cdot 4\cdot confidence\\0.5 \cdot 2\cdot self-awareness\end{bmatrix}").to_corner(UL)
        p3[1][0:2].set_color(PURE_YELLOW)
        p3[2][7:17].set_color(RED)
        p3[2][23:37].set_color(GREEN)
        vec3 = num1.get_vector([2,1], color=PURE_YELLOW)

        self.play(TransformMatchingShapes(p2,p3), run_time=2)
        self.wait(2)
        self.play(Transform(vec2,vec3), run_time=2)
        self.wait()

class VectorAddition(Scene):
    def construct(self):

        num1 = NumberPlane().set_opacity(0.5)
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)

        #build
        self.wait()
        self.play(Write(num1))
        self.play(GrowArrow(ihatvec))
        self.play(GrowArrow(jhatvec))

        #first vector
        vec1 = num1.get_vector([2,1], color=PURE_YELLOW)
        p1 = MathTex(r"P_{1}=\begin{bmatrix}2\cdot confidence\\1\cdot self-awareness\end{bmatrix}").to_corner(UL)
        p1[0][0:2].set_color(PURE_YELLOW)
        p1[0][6:16].set_color(RED)
        p1[0][18:32].set_color(GREEN)

        self.play(GrowArrow(vec1))
        self.play(Write(p1))
        self.wait(6)

        #second vector, placed at tip of first
        vec2 = Vector([2,-1], color=PURE_MAGENTA)
        p2 = MathTex(r"P_{2}=\begin{bmatrix}2\cdot confidence\\-1\cdot self-awareness\end{bmatrix}").to_corner(DL)
        p2[0][0:2].set_color(PURE_MAGENTA)
        p2[0][6:16].set_color(RED)
        p2[0][18:33].set_color(GREEN)

        self.play(GrowArrow(vec2))
        self.wait()
        self.play(Write(p2))
        self.wait(8)

        #resultant vector
        vec_sum = num1.get_vector([4,0], color=WHITE)
        p_sum = MathTex(r"P_{1}+P_{2}=\begin{bmatrix}4\cdot confidence\\0\cdot self-awareness\end{bmatrix}").to_edge(LEFT).shift(-1.5*UP)
        p_sum[0][0:2].set_color(PURE_YELLOW)
        p_sum[0][3:5].set_color(PURE_MAGENTA)
        p_sum[0][9:19].set_color(RED)
        p_sum[0][21:35].set_color(GREEN)

        self.play(vec2.animate.shift(vec1.get_end()), run_time=8)
        self.wait(8)
        self.play(GrowArrow(vec_sum), run_time=4)
        self.wait(7)
        self.play(Unwrite(p1), Unwrite(p2))
        self.wait()
        self.play(Write(p_sum))
        self.wait()

class BasicTransform(Scene):
    def construct(self):

        num1 = NumberPlane()
        num2 = NumberPlane().set_opacity(0.3).set_color(BLUE).set_z_index(-1)
        ihatvec = Vector(2*RIGHT,color=RED).set_z_index(1)
        jhatvec = Vector(2*UP,color=GREEN).set_z_index(1)
        att1 = Tex("discipline").next_to(ihatvec,DOWN).set_color(RED).shift(RIGHT*0.2).set_z_index(1)
        att2 = Tex("independence").next_to(jhatvec,LEFT).set_color(GREEN).shift(DOWN*0.5).set_z_index(1)

        #build
        self.wait()
        self.play(Write(num1))
        self.add(num2)
        self.play(GrowArrow(ihatvec))
        self.play(Write(att1))
        self.wait(5)
        self.play(GrowArrow(jhatvec))
        self.play(Write(att2))
        self.wait(5)

        matrix1 = [[1,1],
                   [0,1]]
        matrix2 = [[1,-1],
                   [0,1]]
        self.play(num1.animate.apply_matrix(matrix=matrix1), run_time=5)
        self.wait(6)
        self.play(num1.animate.apply_matrix(matrix=matrix2), run_time=5)
        self.wait(7)

        #person and change
        p1 = Vector([2,2], color=PURE_YELLOW)
        p1t = Vector([4,2], color=PURE_YELLOW)
        p1tex = MathTex(r"P_{1}").set_color(PURE_YELLOW).move_to(p1).shift(UL*0.4)
        p1change = MathTex(r"P_{1}=\begin{bmatrix}1\\1\end{bmatrix}\to",r"P_{1}=\begin{bmatrix}2\\1\end{bmatrix}").to_corner(UL).set_z_index(1)
        p1change[0][0:2].set_color(PURE_YELLOW)
        p1change[1][0:2].set_color(PURE_YELLOW)

        self.play(GrowArrow(p1))
        self.play(Write(p1tex))
        p1c = p1.copy()
        self.wait(4)
        self.play(num1.animate.apply_matrix(matrix=matrix1), ReplacementTransform(p1,p1t), p1tex.animate.shift(RIGHT*1.3), run_time=5)
        self.wait(5)
        self.play(Write(p1change))
        self.wait(10)
        self.play(num1.animate.apply_matrix(matrix=matrix2), ReplacementTransform(p1t, p1c), p1tex.animate.shift(RIGHT*-1.3), run_time=5)
        self.wait(5)

        #explain trnasformation matrix
        tm1 = MathTex(r"\begin{bmatrix}1\cdot discipline&0\\0&1\cdot independence\\\end{bmatrix}").to_corner(DL)
        tm2 = MathTex(r"\begin{bmatrix}1\cdot discipline&1\\0&1\cdot independence\\\end{bmatrix}").to_corner(DL)
        tm3 = MathTex(r"\begin{bmatrix}1\cdot discipline&1\cdot independence \, builds \, discipline\\0&1\cdot independence\\\end{bmatrix}").to_corner(DL)
        b1 = SurroundingRectangle(tm1, fill_color=BLACK, fill_opacity=1, stroke_opacity=0) 
        b2 = SurroundingRectangle(tm2, fill_color=BLACK, fill_opacity=1, stroke_opacity=0) 
        b3 = SurroundingRectangle(tm3, fill_color=BLACK, fill_opacity=1, stroke_opacity=0) 

        self.play(FadeIn(b1),Write(tm1))
        self.wait(20)
        p1c2 = Vector([4,2], color=PURE_YELLOW)
        self.play(VGroup(num1, jhatvec).animate.apply_matrix(matrix=matrix1), ReplacementTransform(p1c,p1c2), p1tex.animate.shift(RIGHT*1.3),run_time=5)
        self.wait(5)
        self.play(FadeTransform(b1,b2), TransformMatchingShapes(tm1,tm2), run_time=2)
        self.wait(10)
        self.play(FadeTransform(b2,b3), TransformMatchingShapes(tm2,tm3))
        self.wait()

class VectorDotProductLabel(Scene):
    def construct(self):

        dotproduct2 = MathTex(r"P_{1}",r"\cdot",r"P_{2}").scale(1.7)
        dotproduct2[0].set_color(PURE_YELLOW)
        dotproduct2[2].set_color(BLUE)

        dotproduct = Tex("Comparing Identities Between People").shift(UP*2)
        ar1 = Arrow(dotproduct.get_bottom(), dotproduct2[1].get_top())


        #dot product intro
        self.wait()
        self.play(Write(dotproduct2))
        self.wait(3)

        self.play(Write(dotproduct), GrowArrow(ar1), run_time=2)
        self.play(Circumscribe(dotproduct2[1]))
        self.play(Indicate(dotproduct2[1]))

        self.wait()
        self.play(Unwrite(ar1))
        self.wait()
        self.play(dotproduct.animate.to_edge(UP))


        #numberplane visual
        number_plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            x_length=4,
            y_length=4,
        ).move_to(LEFT*4.5).set_opacity(0.7)
        npV1 = number_plane.get_vector([3,2,0]).set_color(PURE_YELLOW)
        npW1 = number_plane.get_vector([4,1,0]).set_color(BLUE)
        npB1 = number_plane.get_vector([1,0]).set_color(PURE_RED)
        npB2 = number_plane.get_vector([0,1]).set_color(PURE_GREEN)

        self.play(Write(number_plane),run_time=2)
        self.wait()

        self.play(GrowArrow(npB1))
        self.play(GrowArrow(npB2))

        self.play(ReplacementTransform(dotproduct2[0].copy(),npV1),run_time=2)
        self.wait()

        self.play(ReplacementTransform(dotproduct2[2].copy(),npW1),run_time=2)

        #calculation
        vectorv = MathTex(r"\begin{bmatrix}3\\2\end{bmatrix}").shift(2*DOWN+LEFT)
        vectorv[0][0].set_color(PURE_YELLOW)
        vectorv[0][3].set_color(PURE_YELLOW)
        vectorv[0][1].set_color(RED)
        vectorv[0][2].set_color(GREEN)
        vectorw = MathTex(r"\begin{bmatrix}4\\1\end{bmatrix}").shift(2*DOWN+RIGHT)
        vectorw[0][0].set_color(BLUE)
        vectorw[0][3].set_color(BLUE)
        vectorw[0][1].set_color(RED)
        vectorw[0][2].set_color(GREEN)
        cdot = MathTex(r"\cdot").shift(2*DOWN)

        self.play(ReplacementTransform(dotproduct2[0].copy(),vectorv))
        self.wait()

        self.play(Write(cdot))
        self.wait()

        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw))

        #calc right side
        equals = MathTex(r"=").shift(2*DOWN+RIGHT*2)
        equation = MathTex(r"3\cdot 4",r"+",r"2\cdot1").shift(2*DOWN+RIGHT*4)
        equation[0].set_color(RED)
        equation[2].set_color(GREEN)
        equationCopy1 = VGroup(vectorv[0][1],vectorw[0][1]).copy()
        equationCopy2 = VGroup(vectorv[0][2],vectorw[0][2]).copy()

        self.wait()
        self.play(Write(equals))
        self.wait()
        self.play(ClockwiseTransform(equationCopy1,equation[0]),run_time=4)
        self.wait()
        self.play(FadeIn(equation[1]))
        self.wait()
        self.play(ClockwiseTransform(equationCopy2,equation[2]),run_time=4)

        result = MathTex(r"=14").next_to(equation, DOWN)
        self.play(Write(result))
        self.wait(5)
        self.play(Unwrite(result))

        #numberplane visual2
        npV2 = number_plane.get_vector([4,4,0]).set_color(PURE_YELLOW)
        npW2 = number_plane.get_vector([-1,-3,0]).set_color(BLUE)

        self.wait(2)
        self.play(ReplacementTransform(npV1,npV2),run_time=2)
        self.wait()
        self.play(ReplacementTransform(npW1,npW2),run_time=2)
        self.wait()

        #calculation2
        vectorv2 = MathTex(r"\begin{bmatrix}4\\4\end{bmatrix}").shift(2*DOWN+LEFT)
        vectorv2[0][0].set_color(PURE_YELLOW)
        vectorv2[0][3].set_color(PURE_YELLOW)
        vectorv2[0][1:2].set_color(RED)
        vectorv2[0][2].set_color(GREEN)
        vectorw2 = MathTex(r"\begin{bmatrix}-1\\-3\end{bmatrix}").shift(2*DOWN+RIGHT)
        vectorw2[0][0].set_color(BLUE)
        vectorw2[0][5].set_color(BLUE)
        vectorw2[0][1:3].set_color(RED)
        vectorw2[0][3:5].set_color(GREEN)

        self.play(Unwrite(VGroup(vectorv,vectorw)))
        self.play(Unwrite(equationCopy1),Unwrite(equationCopy2), Unwrite(equation))
        self.play(ReplacementTransform(dotproduct2[0].copy(),vectorv2))
        self.wait()
        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw2))
        self.wait()

        #calc right side
        equationCopy3 = VGroup(vectorv2[0][1:3],vectorw2[0][1:3]).copy()
        equationCopy4 = VGroup(vectorv2[0][3],vectorw2[0][3]).copy()
        equation2 = MathTex(r"4\cdot -1",r"+",r"4\cdot -3").shift(2*DOWN+RIGHT*4)
        equation2[0].set_color(RED)
        equation2[2].set_color(GREEN)

        self.wait()
        self.play(ClockwiseTransform(equationCopy3,equation2[0]), run_time=3)
        self.wait()
        self.play(FadeIn(equation2[1]))
        self.wait()
        self.play(ClockwiseTransform(equationCopy4,equation2[2]), run_time=3)
        self.wait()

        result2 = MathTex(r"=-16").next_to(equation2, DOWN)
        self.play(Write(result2))
        self.wait(5)

class VectorDotProduct(Scene):
    def construct(self): 

        nump = NumberPlane().set_opacity(0.4)
        v_vec = nump.get_vector([3,1,0],color=PURE_YELLOW)
        w_vec = nump.get_vector([1,3,0],color=RED)
        v_vectex = MathTex(r"P_{1}", color=PURE_YELLOW)
        w_vectex = MathTex(r"P_{2}", color=RED)
        v_vectex.add_updater(lambda mob: mob.move_to(v_vec).shift(RIGHT*0.5 + DOWN*0.5))
        w_vectex.add_updater(lambda mob: mob.move_to(w_vec).shift(LEFT*0.5 + UP*0.5))

        dotproduct = Tex("Comparing Identities").to_corner(UL) 
        dotproduct2 = MathTex(r"P_{1}",r"\cdot",r"P_{2}").next_to(dotproduct,RIGHT)
        dotproduct2[0].set_color(PURE_YELLOW)
        dotproduct2[2].set_color(RED)
        line = Line(start=[-12,-4,0],end=[12,4,0]).set_z_index(-1)

        #init
        self.wait()
        self.play(FadeIn(nump))
        self.wait()
        self.play(GrowArrow(v_vec), FadeIn(v_vectex),run_time=1.5)
        self.play(GrowArrow(w_vec), FadeIn(w_vectex),run_time=1.5)
        self.wait()
        self.play(Write(VGroup(dotproduct,dotproduct2)))


        #geometric projection
        conetctLine = Line(end=[1.8,0.6,0], start=[2*w_vec.get_x(),2*w_vec.get_y(),0])
        projectVector = Vector([0,0,0],color=RED)
        projectVector.add_updater(lambda mob: mob.become(Vector(
            [3*(3*2*w_vec.get_x()+2*w_vec.get_y())/np.sqrt(100),
             1*(3*2*w_vec.get_x()+2*w_vec.get_y())/np.sqrt(100),0],
             color = GREEN
            ).set_opacity(0)))
        # rightan = Angle(conetctLine,line, dot=True, quadrant=(-1,1), other_angle=True)

        # self.wait(3)
        # self.play(GrowFromCenter(line), run_time=3)
        # self.play(Indicate(VGroup(v_vec,v_vectex)))
        # self.wait()
        # self.play(Write(conetctLine), run_time=3)
        # self.wait(2)
        # self.play(ReplacementTransform(w_vec.copy(),projectVector), run_time=0.1)
        self.add(projectVector)
        # self.wait()
        # self.play(GrowFromPoint(rightan, projectVector.get_end()))
        # self.wait(3)

        #equation
        eqation1 = MathTex(r"P_{1}",r"\cdot",r"P_{2}", r">",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation1[0].set_color(PURE_YELLOW)
        eqation1[2].set_color(RED)

        self.play(Write(eqation1))
        self.wait(3)

        #next positions example
        eqation2 = MathTex(r"P_{1}",r"\cdot",r"P_{2}", r"<",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation2[0].set_color(PURE_YELLOW)
        eqation2[2].set_color(RED)
        eqation3 = MathTex(r"P_{1}",r"\cdot",r"P_{2}", r"=",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation3[0].set_color(PURE_YELLOW)
        eqation3[2].set_color(RED)

        # self.play(Unwrite(rightan))
        # self.play(Unwrite(conetctLine))
        # self.wait(3)

        self.play(w_vec.animate.rotate_about_origin(PI), run_time=3)
        self.play(Indicate(eqation1))
        self.play(TransformMatchingShapes(eqation1,eqation2))
        self.wait(6)

        self.play(w_vec.animate.rotate_about_origin(PI+0.6435), run_time=3)
        self.play(Indicate(eqation2))
        self.play(TransformMatchingShapes(eqation2,eqation3))
        self.wait(6)

        #rotation and calc
        dotp = ValueTracker(0)
        dotp.add_updater(lambda mob: mob.set_value(4*(projectVector.get_x()*v_vec.get_x() + projectVector.get_y()*v_vec.get_y())))
        number1 = DecimalNumber(0,num_decimal_places=2).next_to(eqation3[3], RIGHT, buff=0.4)

        self.add(dotp)
        self.play(FadeOut(eqation3[4]))
        self.play(FadeIn(number1))
        self.wait()
        number1.add_updater(lambda mob: mob.set_value(dotp.get_value()))

        self.play(Rotate(w_vec,2*PI,about_point=ORIGIN), rate_func=linear, run_time=7)
        self.play(Rotate(w_vec,-2*PI,about_point=ORIGIN), rate_func=linear, run_time=15)
        self.wait()

class AngleMeassurment(Scene):
    def construct(self): 

        nump = NumberPlane().set_opacity(0.4)
        v_vec = nump.get_vector([3,1,0],color=PURE_YELLOW)
        w_vec = nump.get_vector([1.01,3,0],color=RED)
        v_vectex = MathTex(r"P_{1}", color=PURE_YELLOW)
        w_vectex = MathTex(r"P_{2}", color=RED)
        v_vectex.add_updater(lambda mob: mob.move_to(v_vec).shift(RIGHT*0.5 + DOWN*0.5))
        w_vectex.add_updater(lambda mob: mob.move_to(w_vec).shift(LEFT*0.5 + UP*0.5))

        dotproduct = Tex("Comparing Identities").to_corner(UL) 
        dotproduct2 = MathTex(r"P_{1}",r"\measuredangle",r"P_{2}").next_to(dotproduct,RIGHT)
        dotproduct2[0].set_color(PURE_YELLOW)
        dotproduct2[2].set_color(RED)
        line = Line(start=[-12,-4,0],end=[12,4,0]).set_z_index(-1)

        #init
        self.wait()
        self.play(FadeIn(nump))
        self.wait()
        self.play(GrowArrow(v_vec), FadeIn(v_vectex),run_time=1.5)
        self.play(GrowArrow(w_vec), FadeIn(w_vectex),run_time=1.5)
        self.wait()
        self.play(Write(VGroup(dotproduct,dotproduct2)), run_time=3)
        self.wait(5)

        #angle
        a1 = Angle(v_vec,w_vec, radius=2)

        self.play(Write(a1))
        self.wait(5)
        a1.add_updater(lambda mob: mob.become(Angle(v_vec,w_vec, radius=2)))

        #rotation and calc
        eqation3 = MathTex(r"\theta=").shift(RIGHT*2+DOWN*1.5)
        dotp = ValueTracker(0)
        dotp.add_updater(lambda mob: mob.set_value(4*(v_vec.get_x()*v_vec.get_x() + v_vec.get_y()*v_vec.get_y())))
        number1 = DecimalNumber(0,num_decimal_places=2).next_to(eqation3, RIGHT, buff=0.4)

        self.add(dotp)
        self.play(FadeIn(eqation3))
        self.wait(4)
        self.add(number1)
        number1.add_updater(lambda mob: mob.set_value(
            (-0.5*PI*(normalize(v_vec.get_end())[0] * normalize(w_vec.get_end())[0] + normalize(v_vec.get_end())[1] * normalize(w_vec.get_end())[1]) + 0.5*PI)* 360/(2*PI)
            ))
        self.add(number1)

        self.play(Rotate(w_vec,2*PI,about_point=ORIGIN), rate_func=linear, run_time=8)
        self.play(Rotate(w_vec,-2*PI,about_point=ORIGIN), rate_func=linear, run_time=20)
        self.wait()

class CrossProduct(ThreeDScene):
    def construct(self):
        v1 = Vector([3,0], color=RED)        
        v2 = Vector([0,3], color=GREEN)
        v3 = Vector([3,0], color=BLUE).rotate_about_origin(-PI/2, UP)
        att1 = Tex("rationality").next_to(v1,DOWN).set_color(RED)
        att2 = Tex("emotionality").shift(LEFT*0.6+UP*1.5).set_color(GREEN).rotate(PI/2)
        att3 = Tex("analyticity").set_color(BLUE).rotate(PI/2).rotate(PI/2, UP).next_to(v3, DOWN)

        #build
        self.move_camera(phi=60*DEGREES, zoom=1.5, frame_center=[0,0,1])
        self.begin_ambient_camera_rotation(0.2)
        self.play(Create(v1))
        self.play(Create(v2))
        self.play(Write(att1))
        self.play(Write(att2))
        self.play(Create(v3))
        self.play(Write(att3))
        self.wait(8)

        #persons in space
        p1 = Vector([2,1,1])
        p2 = Vector([2,1,1]).rotate_about_origin(PI/2, [2,1,1])
        p1tex = MathTex(r"P_{1}=\begin{bmatrix}1\cdot rationality\\1\cdot emotionality\\1\cdot analyticity\end{bmatrix}").to_corner(UL)
        p1tex[0][7:18].set_color(RED)
        p1tex[0][20:32].set_color(GREEN)
        p1tex[0][34:45].set_color(BLUE)
        b1 = SurroundingRectangle(p1tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.stop_ambient_camera_rotation()
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=-1, run_time=3)
        self.play(GrowArrow(p1),GrowArrow(p2), run_time=3)
        self.wait(3)
        # self.add_fixed_in_frame_mobjects(b1,p1tex)
        # self.play(FadeIn(b1),Write(p1tex))

        #second person
        p3 = Vector([0,2,2])
        p4 = Vector([0,2,2]).rotate_about_origin(PI/2, [0,2,2])
        p2tex = MathTex(r"finding \, \, a \, \, differnt \, \, person:",r"P_{1} \times P_{2}").to_corner(UL)
        p2tex[1].set_color(PURE_MAGENTA)
        b2 = SurroundingRectangle(p2tex, fill_opacity=0.8, fill_color=BLACK, stroke_opacity=0)

        self.play(GrowArrow(p3),GrowArrow(p4), run_time=3)
        self.wait(3)
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=1, run_time=3)
        self.wait(3)
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=2, run_time=3)

        self.wait(3)
        self.add_fixed_in_frame_mobjects(b2,p2tex)
        self.play(FadeIn(b2),Write(p2tex))
        self.wait(4)

        #new person
        p5 = Vector([0,-2,2]).set_color(PURE_MAGENTA)
        p6 = Vector([0,-2,2]).rotate_about_origin(PI/2, [0,-2,2]).set_color(PURE_MAGENTA)

        self.play(GrowArrow(p5),GrowArrow(p6))
        self.wait(4)
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=1, run_time=3)
        self.wait(2)
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=0, run_time=3)
        self.wait(2)
        self.move_camera(zoom=1, frame_center=[0,0,1], theta=-1, run_time=3)
        self.wait(2)

class Ending(ThreeDScene):
    def construct(self):

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        
        page1 = VGroup(banner,bannertxt)

        download = Tex("Download Link:").set_z_index(1)
        download2 = Tex("github.com/Namitera/English-Identity-From-Linear-Algebra-25.03.2026").scale(0.85).shift(DOWN).set_z_index(1)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(3)

        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*5.5+LEFT*-0))
        self.play(FadeIn(download2))
        self.play(download2.animate.to_corner(UL).shift(DOWN*6.5+LEFT*-0))
        self.wait()
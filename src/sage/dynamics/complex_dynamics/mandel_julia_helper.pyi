from typing import Any, Union

def _color_to_RGB(color: Any) -> tuple[int, int, int]: ...

def fast_mandelbrot_plot(x_center: float, y_center: float, image_width: float, 
                        max_iteration: int, pixel_count: int, level_sep: int, 
                        color_num: int, base_color: Any) -> Any: ...

def fast_external_ray(theta: float, D: int = 30, S: int = 10, R: int = 100, 
                     image_width: float = 4, pixel_count: int = 500, 
                     x_center: float = 0, y_center: float = 0, base_color: Any = None) -> Any: ...

def convert_to_pixels(point_list: list[Any], x_0: float, y_0: float, width: float, 
                     height: float, pixel_count: int) -> list[tuple[int, int]]: ...

def get_line(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]: ...

def fast_julia_plot(c_real: float, c_imag: float, x_center: float = 0, y_center: float = 0, 
                   image_width: float = 4, max_iteration: int = 500, pixel_count: int = 500, 
                   level_sep: int = 1, color_num: int = 30, base_color: Any = None) -> Any: ...

def julia_helper(c_real: float, c_imag: float, x_center: float = 0, y_center: float = 0, 
                image_width: float = 4, max_iteration: int = 500, pixel_count: int = 500, 
                level_sep: int = 1, color_num: int = 30, base_color: Any = None, 
                point_color: Any = None, external_ray: Any = None) -> Any: ...

def polynomial_mandelbrot(f: Any, parameter: Any = None, x_center: float = 0, y_center: float = 0, 
                         image_width: float = 4, max_iteration: int = 500, pixel_count: int = 500, 
                         level_sep: int = 1, color_num: int = 30, base_color: Any = None) -> Any: ...

def general_julia(f: Any, x_center: float = 0, y_center: float = 0, image_width: float = 4, 
                 image_height: float = 4, max_iteration: int = 500, pixel_count: int = 500, 
                 level_sep: int = 1, color_num: int = 30, base_color: Any = None, 
                 point_color: Any = None) -> Any: ...

! Module mandelbrot defined in file mandelbrot.f90

subroutine f90wrap_sample_area(real_start, real_end, imag_start, imag_end, max_iters, width, ret_set, height, n0, n1)
    use mandelbrot, only: sample_area
    implicit none
    
    real, intent(in) :: real_start
    real, intent(in) :: real_end
    real, intent(in) :: imag_start
    real, intent(in) :: imag_end
    integer, intent(in) :: max_iters
    integer, intent(in) :: width
    integer, intent(out), dimension(n0,n1) :: ret_set
    integer, intent(in) :: height
    integer :: n0
    integer :: n1
    ret_set = sample_area(real_start=real_start, real_end=real_end, imag_start=imag_start, imag_end=imag_end, &
        max_iters=max_iters, width=width, height=height)
end subroutine f90wrap_sample_area

! End of module mandelbrot defined in file mandelbrot.f90

module julia_set_mod
    implicit none

    private
    integer, parameter :: max_iters = 255
    real(kind=8), parameter :: max_norm = 2.0D00
    complex(kind=8), parameter :: C = cmplx(-0.622772D00, 0.42193D00, kind=8)

    public :: julia_iterate

contains

    elemental function julia_iterate(z0) result(n)
        implicit none
        complex(kind=8), intent(in) :: z0
        integer :: n
        complex(kind=8) :: z
        z = z0
        n = 0
        do while (abs(z) < max_norm .and. n < max_iters)
            z = z**2 + C
            n = n + 1
        end do
    end function julia_iterate

end module julia_set_mod

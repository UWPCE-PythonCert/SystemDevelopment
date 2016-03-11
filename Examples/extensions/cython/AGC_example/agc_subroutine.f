c
c  Subrooutine to compute an automatic gain control filter.
c
c
      subroutine AGC(nAGC,npts,amp,ampAGC)

CF2PY INTENT(OUT) :: ampAGC
CF2PY INTENT(HIDE) :: npts

      real fmax,amp(npts),absamp(npts),ampAGC(npts)
      integer i,j,npts,nAGC,nAGC2

      do i=1,npts
         ampAGC(i)=0.
         absamp(i)=abs(amp(i))
      enddo

      nAGC2=nAGC/2

      do i=nAGC2+1,npts-nAGC2
         fmax=0.
         do j=i-nAGC2,i+nAGC2
            if (absamp(j).gt.fmax) fmax=absamp(j)
         enddo
         ampAGC(i)=amp(i)/fmax
      enddo

      return

      end


c
c  Program to read in a time series, AGC it, dump out a new time series.
c
c 
c
c
c23456789012345678901234567890123456789012345678901234567890123456789012

      parameter(npts0=1000000)
      character*180 infile,outfile
      real amp(npts0),ampAGC(npts0),ampAGC2(npts0),absamp(npts0)

      print *,'Enter input timeseries'
      read (*,'(a)') infile

      print *,'Enter output filename '
      read (*,'(a)') outfile

      print *,'Enter npts length of AGC window'
      read *,nAGC

      nAGC2=nAGC/2
      nrepeat=20

c--------- read in file & zero out the ampAGC array

      open(4,file=infile)
      do i=1,npts0
         read(4,*,end=201) amp(i)
         ampAGC(i)=0.
         ampAGC2(i)=0.
         absamp(i)=abs(amp(i))
      enddo
201   close(4)
      npts=i-1    

c-------- less code, simpler, waaay slower

      call system_clock(count_rate=icr)
      call system_clock (i1)
      do irepeat=1,nrepeat    !----- loop over it many times, just for timing purposes

         do i=nAGC2+1,npts-nAGC2
            fmax=0.
            do j=i-nAGC2,i+nAGC2
               if (absamp(j).gt.fmax) fmax=absamp(j)
            enddo
            ampAGC(i)=amp(i)/fmax
         enddo

      enddo  !----- do irepeat=1,nrepeat
      call system_clock (i2)
      print *, 'Slow time= ', real(i2-i1)/icr

c--------- Automatic Gain Control
c          Only 'rescan' the window for a max if the previous window's
c          max came from the very first point in it's window.

      call system_clock(count_rate=icr)
      call system_clock (i1)
      do irepeat=1,nrepeat

         fmax=0.
         do i=1,nAGC
            if (absamp(i).gt.fmax) fmax=absamp(i)
         enddo
         ampAGC2(nAGC2+1)=amp(nAGC2+1)/fmax
         do i=nAGC2+2,npts-nAGC2
            j0=i-nAGC2-1
            j1=i-nAGC2
            j2=i+nAGC2
            fmax=max(fmax,absamp(j2))
            if (absamp(j0).eq.fmax) then 
               fmax=0.
               do j=j1,j2
                  if (absamp(j).gt.fmax) fmax=absamp(j)
               enddo
            endif
            ampAGC2(i)=amp(i)/fmax
         enddo

      enddo  !----- do irepeat=1,nrepeat
      call system_clock (i2)
      print *, 'Fast time= ', real(i2-i1)/icr

c--------- write output

      open(4,file=outfile)
      do i=1,npts
         write(4,*) i,amp(i),ampAGC(i),ampAGC2(i)
      enddo
      close(4)

      end


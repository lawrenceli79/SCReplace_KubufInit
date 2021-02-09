    DRSmemset(lpshohou->kubuf, 0, sizeof(kubuf));
    DRSmemset(kubuf_dcont, 0, sizeof(kubuf));
    DRSmemset(&kubuf, 0, sizeof(KUBUF));
    DRSmemset( &kubuf, 0, sizeof(kubuf) );
    DRSmemset( &kubuf, 0, sizeof(kubuf)*MAX );
    lmemset((LPSTR)tempkubuf,0,sizeof(KUBUF)*(kasan_num+1));
    DRSmemset(preKubuf,0,sizeof(preKubuf));
    memset(&pkubuf->kuvol, 0, sizeof(pkubuf->kuvol));
    DRSmemset(&lpshohou->kubuf[ct], 0, sizeof(KUBUF));
    lmemset((LPSTR)d,0,sizeof(KUBUF));
    lmemset((LPSTR)&lpshohou->kubuf[j+1],0,sizeof(KUBUF));

    int a = 0;

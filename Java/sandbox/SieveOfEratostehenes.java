package com.shuzijun.leetcode.sandbox;

import java.util.ArrayList;
import java.util.List;

public class SieveOfEratostehenes {
    public List<Integer> findPrimes(int n) {
        boolean[] isComposite = new boolean[n + 1];
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (isComposite[i]) continue;
            for (int multiple = (int) Math.pow(i, 2); multiple <= n; multiple += i)
                isComposite[multiple] = true;
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 1; i < isComposite.length; i++) {
            if (!isComposite[i])
                primes.add(i);
        }
        return primes;
    }

    public static void main(String[] args) {
        SieveOfEratostehenes sieveOfEratostehenes = new SieveOfEratostehenes();
        List<Integer> primes = sieveOfEratostehenes.findPrimes(10000);
        for (int i = 0; i < primes.size(); i++) {
            if (i % 20 == 0)
                System.out.println("");
            System.out.print(primes.get(i) + ", ");
        }
    }
}

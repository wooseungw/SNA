package com.example.weekeight;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import org.springframework.ui.Model;


@Controller
public class BannerController {
    @Autowired
    BannerRepository bannerRepository;

    @GetMapping("/banner") 
    public String banner(Model model) {

        List<Banner> banners = new ArrayList<Banner>(){{
            add(new Banner("다음", "daum.png", "www.daum.net"));
            add(new Banner("네이버", "naver.png", "www.naver.com"));
        }};
        bannerRepository.saveAll(banners);

        List<Banner> bannerList = bannerRepository.findAll();
        model.addAttribute("banners", bannerList);

        return "banner";
    }
}

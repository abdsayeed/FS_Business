import { Component } from '@angular/core';
import { BusinessData } from '../../services/business-data';
import {ActivatedRoute} from '@angular/router';



@Component({
  selector: 'app-business',
  imports: [],
  providers: [BusinessData],
  templateUrl: './business.html',
  styleUrl: './business.css',
})
export class Business {
  constructor(private route: ActivatedRoute,
   private businessData: BusinessData) {
    ngOnit() {
      this.business_list = this.businessData.getBusinesses(
        this.route.snapshot.paramMap.get('id')
      );
    }
   }

}

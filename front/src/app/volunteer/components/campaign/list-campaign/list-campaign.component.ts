import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Campaign } from 'src/app/shared';
import { CampaignService } from 'src/app/volunteer/services/campaign.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CreateEditCampaignComponent } from '../create-edit-campaign/create-edit-campaign.component';
import { DeleteCampaignComponent } from '../delete-campaign/delete-campaign.component';
import { InspectCampaignComponent } from '../inspect-campaign/inspect-campaign.component';

@Component({
  selector: 'app-list-campaign',
  templateUrl: './list-campaign.component.html',
  styleUrls: ['./list-campaign.component.css']
})
export class ListCampaignComponent implements OnInit, OnDestroy {

  campaigns!: Campaign[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private campaignService: CampaignService) { }

  ngOnInit(): void {
    this.listCampaigns();
    this.subscription = this.campaignService.refreshPage$.subscribe(() => {
      this.listCampaigns();
    });
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }

  listCampaigns() {
    this.isLoading = true;
    this.campaignService.listCampaigns().subscribe({
      next: (response) => {
        this.campaigns = response;
        this.campaigns.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''));
        this.isLoading = false;
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e)
    });
  }

  filterCampaign(event: Event) {
    if (event) {
      if (this.filter !== '') {
        this.campaigns = this.campaigns.filter(
          campaign => campaign.name ? campaign.name.toLowerCase().includes(this.filter.toLowerCase()) : false
        );
      } else {
        this.listCampaigns();
      }
    }
  }

  editCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(CreateEditCampaignComponent, { size: 'lg' });
    modalRef.componentInstance.campaign = campaign;
    modalRef.componentInstance.editMode = true;
  }

  deleteCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(DeleteCampaignComponent, { size: 'md' });
    modalRef.componentInstance.campaign = campaign;
  }

  inspectCampaign(campaign: Campaign) {
    let modalRef = this.modalService.open(InspectCampaignComponent, { size: 'lg' });
    modalRef.componentInstance.campaign = campaign;
  }
}

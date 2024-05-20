import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApproveRefuseSwapComponent } from './approve-refuse-swap.component';

describe('ApproveRefuseSwapComponent', () => {
  let component: ApproveRefuseSwapComponent;
  let fixture: ComponentFixture<ApproveRefuseSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApproveRefuseSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ApproveRefuseSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
